# BINF6200
# Assignment 5 - Question 1
# By Spencer Elliott

# Take filenames from the command line
import sys
codons_file = open(sys.argv[1])
seq_file = open(sys.argv[2])

# Extracting info from the codon table file 
# (Code from lecture 4)
data = {}
for l in codons_file:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value
codons_file.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

# Creating dictionaries of codons with their amino acids, and codons with whether or not they are starts
# (Code from lecture 4)
codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

# Reading in the sequence as one line
seq = ''.join(seq_file.read().split())
seq_file.close()

# Calculate length of the sequence
seqlen = len(seq)

# Function to determine the complement of a nucleotide
def complement(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

# Function to determine the reverse complement of the sequence
def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# Function to translate the DNA sequence into amino acids
def translate(seq):
    aa_sequences = []
    proteins = []
    # Iterate through the 3 forward frames
    for i in range(0,3):
        aa_sequences.append([])
        # For each frame, translate into an amino acid sequence
        for j in range(i,seqlen,3):
            codon = seq[j:j+3]
            # Filter out trailing nucleotides (codons must be 3 bases)
            if len(codon) == 3:
                aa = codons[codon]
                aa_sequences[i].append(aa)
        # Join the list of amino acid sequences into a string
        proteins.append([])
        proteins[i] = ''.join(aa_sequences[i])
    return proteins

# Translate the sequence in each frame
proteins = translate(seq)
# Translate in each reverse (complement) frame
rc_seq = reverseComplement(seq)
rc_proteins = translate(rc_seq)

# Printing results
print("Codon table:", sys.argv[1])
print("Sequence:", sys.argv[2], ",", seqlen, "bases")
print("Protein frame 0:", proteins[0])
print("Protein frame 1:", proteins[1])
print("Protein frame 2:", proteins[2])
print("Reverse protein frame 0:", rc_proteins[0])
print("Reverse protein frame 1:", rc_proteins[1])
print("Reverse protein frame 2:", rc_proteins[2])
