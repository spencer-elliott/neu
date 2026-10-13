#!/bin/bash
for chr in PccAS_01_v3 PccAS_02_v3 PccAS_03_v3
do
    grep "^${chr}" PccAS_sample.gff3 > "${chr}.gff3"
    echo "${chr} done"
done
