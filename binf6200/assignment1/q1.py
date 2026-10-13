# BINF6200
# Assignment 1 - Question 1
# By Spencer Elliott

codon = "ATG"

# Use negative string indexing to print characters in reverse
codon_backwards = codon[-1] + codon[-2] + codon[-3]

# Print as lowercase with the .lower() method
print(codon_backwards.lower())
