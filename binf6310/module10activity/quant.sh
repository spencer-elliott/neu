#!/bin/bash
# quant.sh: run kallisto quant on every sample listed in samples.tsv.
# Run it from your module10 folder, inside an srun session with 4 CPUs:
#     bash quant.sh

DATA=/courses/BINF6310.202710/data/q.wan/module10
KALLISTO="apptainer exec -B /courses $DATA/containers/kallisto_0.52.0--hd638d68_1.sif kallisto"

mkdir -p quant      # kallisto makes quant/<sample> only if quant/ already exists

# tail -n +2 skips the header line; read splits each line into the four columns
tail -n +2 samples.tsv | while read sample run condition geo; do
    echo "== $sample: $run ($condition)"
    $KALLISTO quant -t 4 -i $DATA/index/human_sars2.idx \
        -o quant/$sample \
        --single -l 200 -s 30 --rf-stranded \
        $DATA/reads/$run.fastq.gz
done
