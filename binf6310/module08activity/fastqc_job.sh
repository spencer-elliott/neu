#!/bin/bash
#SBATCH --job-name=module08
#SBATCH --partition=courses
#SBATCH --time=00:15:00
#SBATCH --mem=2G
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

FASTQC_CONTAINER=/scratch/${USER}/module08/fastqc_0.12.1--hdfd78af_0.sif
MULTIQC_CONTAINER=/courses/BINF6310.202710/shared/multiqc-latest.sif
DATA=/courses/BINF6310.202710/data/q.wan/module08

mkdir -p fastqc_out
apptainer run -B /courses ${FASTQC_CONTAINER} \
    fastqc -o fastqc_out ${DATA}/*.fastq.gz

apptainer run ${MULTIQC_CONTAINER} \
    multiqc fastqc_out -o multiqc_out
