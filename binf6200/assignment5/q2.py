# BINF6200
# Assignment 5 - Question 2
# By Spencer Elliott

# This file prints a DNA sequence with its reverse complement.
# Command line example: python3 q2.py anthrax_sasp.nuc

# Take a sequence filename from the user
import sys
seq_file = open(sys.argv[1])

# Join file contents into a sequence string
seq = ''.join(seq_file.read().split())
seq_file.close()

# New function to determine the reverse complement of the sequence
def reverseComplement(seq):
    complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    # If nucleotide is not found, return the same thing
    newseq = ''.join([complements.get(nuc, nuc) for nuc in seq.upper()[::-1]])
    return newseq

print("Sequence:", seq)
print("Reverse complement:", reverseComplement(seq))
