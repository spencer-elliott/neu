# BINF6200
# In-Class Exercises, Module 1 - Question 4
# By Spencer Elliott

dna = "gatcaaagtaaac"

rna = dna.replace("t", "u")
number_of_A = rna.count("a")

print(rna + "A" * number_of_A)
