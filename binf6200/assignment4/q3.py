# BINF6200
# Assignment 4 - Question 3
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

# Determining the first amino acid, and whether it is a start
first_codon = seq[0:3]
first_codon_id = codons[first_codon]
if init[first_codon] == True:
    first_codon_start = "yes"
else:
    first_codon_start = "no"

# Translating the whole sequence
# (Code from lecture 4)
seqlen = len(seq)
aaseq = []
# Check if the sequence length is not divisible by 3 (invalid protein)
valid_protein = True
if seqlen % 3 != 0:
    valid_protein = False
else:
    for i in range(0,seqlen,3):
        codon = seq[i:i+3]
        aa = codons[codon]
        aaseq.append(aa)
    protein = ''.join(aaseq)

# Printing results
if valid_protein == False:
    print("Unable to translate sequence - length is not a multiple of 3.")
else:
    print("Codon table:", sys.argv[1])
    print("Sequence:", sys.argv[2], ",", seqlen, "bases")
    print("Protein:", protein)
    print("First codon:", first_codon_id)
    print("Valid start codon:", first_codon_start)
