# BINF6200
# Assignment 9 - Module with DNA sequence class and methods
# By Spencer Elliott

# This module contains a DNA sequence class with various methods from the lecture and previous assignments.

class DNASeq:
    # Initialize with the option to include the sequence and name
    def __init__(self,seq="",name=""):
        self.seq = seq
        self.name = name

    # Method to read in the sequence from a file
    def read(self,filename):
        self.seq = ''.join(open(filename).read().split())

    # Method returning the sequence in reverse
    def reverse(self):
        return self.seq[::-1]

    # Method returning the complement of the sequence
    def complement(self):
        d = {'A':'T','C':'G','G':'C','T':'A'}
        return ''.join(d.get(base, base) for base in self.seq)

    # Method returning the reverse complement of the sequence
    def reverseComplement(self):
        return ''.join(reversed(self.complement()))

    # Method returning the length of the sequence
    def length(self):
        return len(self.seq)

    # Method to find the frequency of a nucleotide in the sequence
    def freq(self,nuc):
        return self.seq.count(nuc)

    # Method to find the G/C content of the sequence
    def percentGC(self):
        gccount = self.freq('C') + self.freq('G')
        return 100*float(gccount)/self.length()

    # Method returning the name and sequence as a string in two lines
    def __str__(self):
        asstr = ">"+self.name+"\n"+self.seq
        return asstr
    
