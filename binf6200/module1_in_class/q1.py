# BINF6200
# In-Class Exercises, Module 1 - Question 1
# By Spencer Elliott

dna = "gcatgacgttattacgactctgtgtggcgtctgctggg"

number_of_N = len(dna) - 6

print(dna[0:3] + "N" * number_of_N + dna[-3:])
