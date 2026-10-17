# Module 05 slides - Class Review Exercises
# 2. Write a program to determine if a DNA sequence provided 
#    in a file contains any invalid symbols.

import sys

# Take the file name from user input
seq_file = open(sys.argv[1])

# Read the sequence
seq = ''.join(seq_file.read().split())

# Iterate and look for invalid symbols
valid_seq = True
for nuc in seq:
    nuc = nuc.upper()
    if nuc not in "ACGT":
        valid_seq = False

# Print result
if valid_seq == True:
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence")
