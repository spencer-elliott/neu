# BINF6200
# Assignment 3 - Question 1
# By Spencer Elliott

# Human gene I chose: PTPN1 (PrimerBank ID: 18104977c1)
primer_forward = "GCAGATCGACAAGTCCGGG"
primer_reverse = "GCCACTCTACATGGGAAGTCAC"

# Function (from lecture) to find the complement of a nucleotide
def complement(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Function (from lecture) to find the reverse complement of a sequence
def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

print("Forward primer:", primer_forward)
print("Reverse complement of forward primer:", reverseComplement(primer_forward))
print("Reverse primer:", primer_reverse)
print("Reverse complement of reverse primer:", reverseComplement(primer_reverse))
