# de.R: from read counts to differentially expressed genes, with DESeq2.
# Run it from your module10 folder, inside the DESeq2 container:
#     Rscript de.R kallisto    uses your kallisto output in quant/       -> writes de_kallisto/
#     Rscript de.R ncbi        uses NCBI's count matrix for the same six samples -> writes de_ncbi/

suppressPackageStartupMessages({
  library(DESeq2)
  library(ggplot2)
})
DATA <- "/courses/BINF6310.202710/data/q.wan/module10"
route <- commandArgs(trailingOnly = TRUE)[1]
if (is.na(route) || !route %in% c("kallisto", "ncbi")) stop("say which counts to use: Rscript de.R kallisto  (or ncbi)")
outdir <- paste0("de_", route)
dir.create(outdir, showWarnings = FALSE)

# ---- 1. The sample table: one row per sample --------------------------------
samples <- read.delim("samples.tsv")
rownames(samples) <- samples$sample
samples$condition <- factor(samples$condition, levels = c("mock", "infected"))

# ---- 2. The count table: one row per gene, one column per sample -------------
if (route == "kallisto") {
  tx2gene <- read.delim(file.path(DATA, "index", "tx2gene.tsv"))
  counts <- sapply(samples$sample, function(s) {
    ab <- read.delim(file.path("quant", s, "abundance.tsv"))
    gene <- tx2gene$gene_name[match(ab$target_id, tx2gene$transcript_id)]
    rowsum(ab$est_counts, gene)[, 1]          # add up the transcripts of each gene
  })
  counts <- round(counts)                      # DESeq2 takes whole numbers
} else {
  ncbi <- read.delim(file.path(DATA, "ncbi", "GSE147507_raw_counts_GRCh38.p13_NCBI.tsv.gz"),
                     row.names = 1, check.names = FALSE)
  annot <- read.delim(file.path(DATA, "ncbi", "Human.GRCh38.p13.annot.tsv.gz"), quote = "")
  symbol <- annot$Symbol[match(rownames(ncbi), annot$GeneID)]
  counts <- rowsum(as.matrix(ncbi[, samples$geo]), symbol)   # NCBI's columns are named by GSM
  colnames(counts) <- samples$sample
}
write.table(data.frame(gene = rownames(counts), counts, check.names = FALSE),
            file.path(outdir, "gene_counts.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
cat("Count table:", nrow(counts), "genes x", ncol(counts), "samples\n")
cat("Reads counted per sample (millions):", round(colSums(counts) / 1e6, 2), "\n")

# ---- 3. DESeq2 --------------------------------------------------------------
dds <- DESeqDataSetFromMatrix(countData = counts, colData = samples, design = ~ condition)
dds <- dds[rowSums(counts(dds) >= 10) >= 3, ]  # keep genes with 10 or more reads in at least 3 samples
dds <- DESeq(dds)
res <- results(dds, contrast = c("condition", "infected", "mock"), alpha = 0.05)
cat("\nSize factors:", round(sizeFactors(dds), 2), "\n")
summary(res)

# ---- 4. The results table, sorted by adjusted p-value -----------------------
full <- data.frame(gene = rownames(res), as.data.frame(res))
full <- full[order(full$padj, -abs(full$stat)), ]
out <- data.frame(gene = full$gene, round(full[, c("baseMean", "log2FoldChange", "lfcSE", "stat")], 3),
                  pvalue = signif(full$pvalue, 3), padj = signif(full$padj, 3))   # rounded for reading
write.table(out, file.path(outdir, "results.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
tested <- full[!is.na(full$padj), ]                                               # the cutoffs use the exact values
up <- tested$gene[tested$padj < 0.05 & tested$log2FoldChange > 1]
writeLines(up, file.path(outdir, "up_genes.txt"))
writeLines(tested$gene, file.path(outdir, "background.txt"))
cat("\nGenes tested:", nrow(tested), "  padj < 0.05:", sum(tested$padj < 0.05),
    "  of those up more than 2x:", length(up), "\n")
cat("\nTop 20 genes by adjusted p-value:\n")
print(head(out, 20), row.names = FALSE)
key <- c("SARS-CoV-2", "IFNB1", "IFNL1", "IFIT1", "MX1", "CXCL10")
cat("\nGenes to check:\n")
print(out[match(intersect(key, out$gene), out$gene), ], row.names = FALSE)

# ---- 5. PCA plot ------------------------------------------------------------
vsd <- vst(dds, blind = TRUE)
pca <- plotPCA(vsd, intgroup = "condition", returnData = TRUE)
pv <- round(100 * attr(pca, "percentVar"))
p <- ggplot(pca, aes(PC1, PC2, colour = condition, label = name)) +
  geom_point(size = 3) + geom_text(vjust = -1, size = 3.5, show.legend = FALSE) +
  scale_x_continuous(expand = expansion(mult = 0.15)) + scale_y_continuous(expand = expansion(mult = 0.2)) +
  labs(x = paste0("PC1: ", pv[1], "% of variance"), y = paste0("PC2: ", pv[2], "% of variance"),
       title = paste("PCA,", route, "counts")) + theme_bw()
ggsave(file.path(outdir, "pca.png"), p, width = 6, height = 4.5, dpi = 150)
cat("\nPC1:", pv[1], "%   PC2:", pv[2], "%\n")

# ---- 6. Volcano plot --------------------------------------------------------
y <- -log10(pmax(tested$padj, 1e-300))
col <- ifelse(tested$padj < 0.05 & tested$log2FoldChange > 1, "firebrick",
              ifelse(tested$padj < 0.05 & tested$log2FoldChange < -1, "steelblue", "grey70"))
png(file.path(outdir, "volcano.png"), width = 900, height = 700, res = 130)
plot(tested$log2FoldChange, y, pch = 20, cex = 0.6, col = col,
     xlab = "log2 fold change (infected / mock)", ylab = "-log10 adjusted p-value",
     main = paste("Volcano plot,", route, "counts"))
abline(v = c(-1, 1), h = -log10(0.05), lty = 2, col = "grey40")
lab <- tested$gene %in% c("SARS-CoV-2", "IFNB1", "IFNL1", "IFIT2", "CXCL10", "IL6")
text(tested$log2FoldChange[lab], y[lab], tested$gene[lab], cex = 0.8,
     pos = ifelse(tested$gene[lab] == "SARS-CoV-2", 2, 4))   # the virus is at the right edge: its name goes on the left
invisible(dev.off())
cat("Wrote", file.path(outdir, c("gene_counts.tsv", "results.tsv", "up_genes.txt", "background.txt", "pca.png", "volcano.png")), sep = "\n  ")
