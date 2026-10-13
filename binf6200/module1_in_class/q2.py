# BINF6200
# In-Class Exercises, Module 1 - Question 2
# By Spencer Elliott

dna  = "ttcggagaattcactgacgaattcggt"
site = "GAATTC"

dna = dna.upper()
dna = dna.replace(site, "[" + site + "]")

print(dna)
