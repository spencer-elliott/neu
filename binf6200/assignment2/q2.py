# BINF6200
# Assignment 2 - Question 2
# By Spencer Elliott

# Codon to calculate the reverse complement for
codon = "ATG"

# Function to find the complement of a nucleotide
def complement(nuc):
    # Ensure that the nucleotide is always converted to upper case
    nuc = nuc.upper()
    if nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'C':
        comp = 'G'
    elif nuc == 'G':
        comp = 'C'
    else:
        comp = nuc
    return comp

# Function to find the reverse complement of a codon
def reverse_complement(codon):
    # First, reverse the codon
    codon_reverse = codon[::-1]
    # Then each nucleotide in the codon becomes its complement
    reverse_complement = ""
    for i in range(3):
        reverse_complement += complement(codon_reverse[i])
    return reverse_complement

print("Reverse complement of " + codon + ": " + reverse_complement(codon))
