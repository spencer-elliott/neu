# BINF6200
# Assignment 3 - Question 2
# By Spencer Elliott

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

# Function to check for a reverse complement palindrome
def isPalindrome(seq):
    reverse_comp = reverseComplement(seq)
    # Compare the sequence against its reverse complement
    if seq.upper() == reverse_comp:
        return seq + " is a reverse complement palindrome!"
    else:
        return seq + " is not a reverse complement palindrome."

print(isPalindrome("TTGAGTAGACGCGTCTACTCAA"))
print(isPalindrome("TTGAGTAGACGTCGTCTACTCAA"))
print(isPalindrome("ATATATATATATATAT"))
print(isPalindrome("ATCTATATATATGTAT"))
