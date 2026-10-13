# BINF6200
# Assignment 4 - Question 1
# By Spencer Elliott

# Take filename from the command line and open
import sys
primers = open(sys.argv[1])

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

# Go through each line in the file
for line in primers:
    # Split the line into words
    line = line.split()
    # Take the first two words (the primers)
    primer_forward = line[0]
    primer_reverse = line[1]
    # Print the reverse complements
    print(reverseComplement(primer_forward), reverseComplement(primer_reverse))

# Close the file    
primers.close()
