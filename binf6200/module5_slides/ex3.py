# Module 05 slides - Class Review Exercises
# 3. Write a program to count the proportion of each symbol in a
#    DNA sequence, provided in a file.

import sys

# Take the file name from user input
seq_file = open(sys.argv[1])

# Read the sequence
seq = ''.join(seq_file.read().split())

# Determine the sequence length
length = len(seq)

# Calculate the proportion of each symbol in the sequence
seq = seq.upper()
proportion_A = seq.count("A") / length
proportion_C = seq.count("C") / length
proportion_G = seq.count("G") / length
proportion_T = seq.count("T") / length

# Print result
print("DNA sequence nucleotide proportions:")
print("A:", round(proportion_A, 2))
print("C:", round(proportion_C, 2))
print("G:", round(proportion_G, 2))
print("T:", round(proportion_T, 2))
