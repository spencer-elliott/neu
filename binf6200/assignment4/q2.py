# BINF6200
# Assignment 4 - Question 2
# By Spencer Elliott

# Some test sequences to perform a comparison
seq1 = "ACTGCTGATCGATAGCTACGATCG"
seq2 = "ACTgCTGNATCGATAGCTacXGATCG"
seq3 = "ACT GCTG  ATCGATAGC TACGATCG"

# Method 1: .find() method into a parallel string
def complement_method1(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp
# The .find() method has to look through the strings one by one in order to pair a base with its correct complement.
# This method would not return the complement of a lower case base. Putting the .upper() method in reverse complement function ensures this can never happen.
# Without the final check, .find() would return -1, giving the wrong base (last character of complements) and continue silently running without raising any error.

# Method 2: Chain of if/elif
def complement_method2(nuc):
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
# The .find() method has to go through each part of the conditional statement until it finds the correct complement, which is pretty clunky.
# This method would not return the complement of a lower case base. Putting the .upper() method in reverse complement function ensures this can never happen.
# The else statement ensures that anything that isn't a base (ex. "N") will remain as-is.

# Method 3: Dictionary of bases and complements
def complement_method3(nuc):
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    comp = d.get(nuc, nuc)
    return comp
# The dictionary has an entry for each nucleotide and goes right to its complement, which is very efficient.
# This method would not return the complement of a lower case base. Putting the .upper() method in reverse complement function ensures this can never happen.
# Using the d.get() method, with the nucleotide itself as a fallback, will handle anything that isn't an approved base.

# I think that I would understand each of these methods if I returned to them later, but the dictionary seems the most elegant and straightforward.
# The dictionary data type is best suited to the purpose of looking up values that are paired with something else, like nucleotides and their complements.

# Function to print the reverse complement using each method
def reverseComplement(seq):
    seq = seq.upper()
    newseq_method1 = ""
    newseq_method2 = ""
    newseq_method3 = ""
    for nuc in seq:
        newseq_method1 = complement_method1(nuc) + newseq_method1
        newseq_method2 = complement_method1(nuc) + newseq_method2
        newseq_method3 = complement_method1(nuc) + newseq_method3
    print("Method 1:", newseq_method1)
    print("Method 2:", newseq_method2)
    print("Method 3:", newseq_method3)

print("Example 1: Standard sequence")
reverseComplement(seq1)
print("Example 2: Sequence with lower case + unknown bases")
reverseComplement(seq2)
print("Example 3: Sequence with spaces")
reverseComplement(seq3)
