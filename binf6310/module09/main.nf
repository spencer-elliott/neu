// Assemble paired-end reads with SPAdes, then check the assembly with QUAST.

params.reads     = "/courses/BINF6310.202710/data/q.wan/module09/mutant_{R1,R2}.fastq"
params.reference = "/courses/BINF6310.202710/data/q.wan/module09/wildtype.fna"
params.outdir    = "results"

process SPADES {
    container '/courses/BINF6310.202710/data/q.wan/module09/containers/spades_4.3.0--hde4eca7_2.sif'
    cpus 4
    memory '8 GB'
    publishDir "${params.outdir}/spades", mode: 'copy'

    input:
    tuple val(sample), path(reads)

    output:
    tuple val(sample), path("${sample}_contigs.fasta")

    script:
    """
    spades.py -1 ${reads[0]} -2 ${reads[1]} -o spades_out -t ${task.cpus} -m 8
    cp spades_out/contigs.fasta ${sample}_contigs.fasta
    """
}

process QUAST {
    container '/courses/BINF6310.202710/data/q.wan/module09/containers/quast_5.3.0--py313pl5321h5ca1c30_2.sif'
    publishDir "${params.outdir}/quast", mode: 'copy'

    input:
    tuple val(sample), path(contigs)
    path reference

    output:
    path "${sample}_quast"

    script:
    """
    quast.py --min-contig 500 -o ${sample}_quast -r ${reference} ${contigs}
    """
}

workflow {
    reads_ch = Channel.fromFilePairs(params.reads)
    SPADES(reads_ch)
    QUAST(SPADES.out, file(params.reference))
}
