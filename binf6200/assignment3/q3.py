# BINF6200
# Assignment 3 - Question 3
# By Spencer Elliott

# run: python3 q3.py GCAGATCGACAAGTCCGGG GCCACTCTACATGGGAAGTCAC

import sys

# Taking the two primers as command line arguments
primer_forward = sys.argv[1]
primer_reverse = sys.argv[2]

# Function (from lecture) to find the complement of a nucleotide
def complement(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Function (from lecture) to find the reverse complement of a sequence
def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

print("Forward primer:", primer_forward)
print("Reverse complement of forward primer:", reverseComplement(primer_forward))
print("Reverse primer:", primer_reverse)
print("Reverse complement of reverse primer:", reverseComplement(primer_reverse))
