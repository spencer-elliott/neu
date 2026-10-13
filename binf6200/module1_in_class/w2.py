# BINF6200
# In-Class Exercises, Module 1 - Warmup 2
# By Spencer Elliott

dna = "gcatgacgttattacgactctgtgtggcgtctgctggg"

length = len(dna)
full_codons = length // 3
leftover_bases = length % 3

print("Full codons:", full_codons)
print("Leftover bases:", leftover_bases)
