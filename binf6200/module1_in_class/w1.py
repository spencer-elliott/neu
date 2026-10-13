# BINF6200
# In-Class Exercises, Module 1 - Warmup 1
# By Spencer Elliott

dna = "gcatgacgttattacgactctgtgtggcgtctgctggg"

length = len(dna)
g_content = dna.count("g")
c_content = dna.count("c")
gc_content = (g_content + c_content) / length * 100
gc_content = round(gc_content, 1)

print("Length:", length)
print("G:", g_content, "C:", c_content)
print("GC content:", gc_content)
