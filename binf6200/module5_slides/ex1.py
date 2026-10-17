# Module 05 slides - Class Review Exercises
# 1. Write a program to determine the length of a DNA sequence provided in a file.

import sys

# Take the file name from user input
seq_file = open(sys.argv[1])

# Read the sequence
seq = ''.join(seq_file.read().split())

# Determine sequence length
length = len(seq)

# Print result
print("DNA sequence length:", length)
