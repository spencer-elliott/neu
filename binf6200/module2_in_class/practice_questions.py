# BINF6200
# In-Class Exercises, Module 2 - Practice Questions
# By Spencer Elliott

# 1) Validate DNA
def is_dna(seq):
    seq_upper_case = seq.upper()
    dna_check = True
    for char in seq_upper_case:
        if char not in 'GCAT':
            dna_check = False
    return dna_check        

# 2) GC statistics & classification
def gc_report(seq, high_threshold):
    seq_upper_case = seq.upper()
    gc_count = seq_upper_case.count('G') + seq_upper_case.count('C')
    gc_fraction = gc_count / len(seq)
    if gc_fraction >= high_threshold:
        return "GC=" + str(gc_fraction) + " -> HIGH"
    else:
        return "GC=" + str(gc_fraction) + " -> LOW"

# 3) RNA trail trimmer
def trim_rna_poly_u(dna):
    dna_lower_case = dna.lower()
    rna = dna_lower_case.replace("t", "u")
    rna_stripped = rna.rstrip("u")
    return rna_stripped

# Testing the functions
seq = "AGTCGATCGTAGCT"
print(is_dna(seq))
print(gc_report(seq, 0.3))
print(trim_rna_poly_u(seq))
