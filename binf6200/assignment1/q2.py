# BINF6200
# Assignment 1 - Question 2
# By Spencer Elliott

sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

# Ensure the sequence is all upper case
sequence_upper_case = sequence.upper()

# Find the position of start codon
start_position = sequence_upper_case.find("ATG")
print(start_position)

# Find the translation frame as the remainder when divided by 3
# String indexing starts at 0, so we need to add 1 first
translation_frame = (start_position % 3) + 1
print(translation_frame)
