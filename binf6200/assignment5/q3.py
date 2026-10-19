# BINF6200
# Assignment 5 - Question 3
# By Spencer Elliott

# This file prints the frequency of each nucleotide in a DNA sequence.
# Command line example: python3 q3.py anthrax_sasp.nuc

# Take a sequence filename from the user
import sys
seq_file = open(sys.argv[1])

# Join file contents into a sequence string
seq = ''.join(seq_file.read().split())
seq_file.close()

# Dictonary to keep track of counts
freq = {}
# For each nucleotide, add 1 to its count if it is already in the dictionary
# If it is new, make a default count of 0 and then add 1
for nuc in seq:
    freq[nuc] = freq.get(nuc, 0) + 1

# Print the results (lambda function from lecture slides)
for nuc, f in sorted(freq.items(), key=lambda p: -p[1]):
    print(nuc, f, round(f / len(seq), 3))
print("Total:", len(seq))
