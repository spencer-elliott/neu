# BINF6200
# In-Class Exercises, Module 1 - Question 3
# By Spencer Elliott

dna  = "cccggaattctagcctt"
site = "GAATTC"

dna = dna.upper()
index = dna.find(site)
site_end = index + len(site)

print("Index:", index)
print("Left: " + dna[:index])
print("Right: " + dna[site_end:])
