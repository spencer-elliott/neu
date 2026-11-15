# BINF6200
# Assignment 9 - Module with codon table class and methods
# By Spencer Elliott

# This module contains a codon table class with various methods from the lecture and previous assignments.

class codon_table:
    # Initialize with an empty codon table
    def __init__(self):
        self.table = {}

    # Method to read in a codon file and create the dictionary
    def read(self,filename):
        try:
            f = open(filename)
        except FileNotFoundError:
            print("Error: could not find codon file", filename)
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

        n = len(aa)
        for i in range(n):
            codon = b1[i] + b2[i] + b3[i]
            isInit = (st[i] == 'M')
            self.table[codon] = (aa[i],isInit)

    # Method to return the amino acid associated with a codon in the codon table
    def amino_acid(self,codon):
        try:
            aa, is_init = self.table[codon]
        except KeyError:
            return 'X'
        return aa

    # Method to determine whether or not a codon is a start in the codon table
    def is_init(self,codon):
        try:
            aa, is_init = self.table[codon]
        except KeyError:
            return 'X'
        return is_init

    # Method to return the amino acid associated with an ambiguous codon (containing N's), or X
    def get_ambig_aa(self,codon):
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
                    codon_set.add(self.table[n1 + n2 + n3][0])

        # If there is only one possible amino acid, return it
        if len(codon_set) == 1:
            aa = codon_set.pop()
        # Otherwise, return X
        else:
            aa = 'X'
        return aa

    # Method to return whether a given sequence begins with a start codon
    def startswith_init(self,seq):
        first_codon = seq.seq[0:3]
        result = (self.is_init(first_codon) == True)
        return result

    # Method to translate a given DNA sequence into amino acids
    def translate(self,seq,frame):
        aa_list = []
        # For each reading frame, translate into an amino acid sequence
        for i in range(frame-1, len(seq.seq), 3):
            codon = seq.seq[i:i+3]
            # Filter out trailing nucleotides (codons must be 3 bases)
            if len(codon) == 3:
                # Check for N as a nucleotide
                if codon[0] == 'N' or codon[1] == 'N' or codon[2] == 'N':
                    aa = self.get_ambig_aa(codon)
                else:
                    aa = self.amino_acid(codon)
                # Add the amino acid to the sequence
                aa_list.append(aa)
        # Join the list of amino acid sequences into a string
        aaseq = ''.join(aa_list)
        return aaseq

    