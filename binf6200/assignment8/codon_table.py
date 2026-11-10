# BINF6200
# Assignment 8 - Module with codon table functions
# By Spencer Elliott

# This is a Python module with codon functions based on Assignment 5 and the most recent lecture.

# Function to read in a codon file and create a dictionary (from lecture 8)
def read_codons_from_filename(codonfile):
    # Try/except block: Make sure the file exists
    try:
        f = open(codonfile)
    except FileNotFoundError:
        print("Error: could not find codon file", codonfile)
        return None
    data = {}
    for l in f:
        sl = l.split()
        key = sl[0]
        value = sl[2]
        data[key] = value
    f.close()

    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']

    codon_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        isInit = (st[i] == 'M')
        codon_table[codon] = (aa[i],isInit)
    return codon_table

# Function to find the amino acid associated with a codon in a given codon table
def amino_acid(codon_table, codon):
    # Try/except block: Make sure the codon is in the table
    try:
        amino_acid, is_init = codon_table[codon]
    except KeyError:
        return 'X'
    return amino_acid

# Function to find whether a codon is a start in a given codon table
def is_init(codon_table, codon):
    # Try/except block: Make sure the codon is in the table
    try:
        amino_acid, is_init = codon_table[codon]
    except KeyError:
        return 'X'
    return is_init

# Function to return the amino acid associated with an ambiguous codon (containing N's), or X
def get_ambig_aa(codon_table, codon):
    # Track the possible nucleotides at each position (if N, it can be any of the four)
    if codon[0] == 'N':
        first = 'ACGT'
    else:
        first = codon[0]
    if codon[1] == 'N':
        second = 'ACGT'
    else:
        second = codon[1]
    if codon[2] == 'N':
        third = 'ACGT'
    else:
        third = codon[2]

    # Make the set of possible amino acids based on the possible nucleotides
    codon_set = set()
    for n1 in first:
        for n2 in second:
            for n3 in third:
                codon_set.add(codon_table[n1 + n2 + n3][0])

    # If there is only one possible amino acid, return it
    if len(codon_set) == 1:
        aa = codon_set.pop()
    # Otherwise, return X
    else:
        aa = 'X'
    return aa

# Function to translate a DNA sequence into amino acids
def translate(codon_table, seq, frame):
    aa_sequence = []
    # For each reading frame, translate into an amino acid sequence
    for i in range(frame-1, len(seq), 3):
        codon = seq[i:i+3]
        # Filter out trailing nucleotides (codons must be 3 bases)
        if len(codon) == 3:
            # Check for N as a nucleotide
            if codon[0] == 'N' or codon[1] == 'N' or codon[2] == 'N':
                aa = get_ambig_aa(codon_table, codon)
            else:
                aa = amino_acid(codon_table, codon)
            # Add the amino acid to the sequence
            aa_sequence.append(aa)
    # Join the list of amino acid sequences into a string
    protein = ''.join(aa_sequence)
    return protein
