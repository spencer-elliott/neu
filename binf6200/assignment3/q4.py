# BINF6200
# Assignment 3 - Question 4
# By Spencer Elliott

# run: python3 q4.py [DNA sequence file] [command]
# Recognized commands: complement, reverse, reversecomplement
# Test sequence file: anthrax_sasp.nuc

import sys
seq_file = sys.argv[1]
command = sys.argv[2].lower()

# Opening the sequence file (command from lecture)
input_seq = ''.join(open(seq_file).read().split())

# Function (from lecture) to find the complement of a nucleotide
def complementNuc(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Function (from lecture) to find the reverse complement of a sequence
def reverseComplementSeq(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complementNuc(nuc) + newseq
    return newseq

# Function to find the complement of a sequence, while keeping the same order
def complementSeq(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq += complementNuc(nuc)
    return newseq

# Function to reverse the order of a sequence
def reverseSeq(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = nuc + newseq
    return newseq

if command == "complement":
    print("Sequence:", input_seq)
    print("Complement:", complementSeq(input_seq))
elif command == "reverse":
    print("Sequence:", input_seq)
    print("Reverse:", reverseSeq(input_seq))
elif command == "reversecomplement":
    print("Sequence:", input_seq)
    print("ReverseComplement:", reverseComplementSeq(input_seq))
else:
    print("Command not recognized.")
