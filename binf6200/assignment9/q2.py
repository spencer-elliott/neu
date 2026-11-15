# BINF6200
# Assignment 9 - Question 2
# By Spencer Elliott

# Translates an amino-acid sequence in all six-frames, using the DNA sequence and codon table modules.
# This time the modules contain their respective classes and the functions are now called as methods.

# Usage example: python3 q1.py standard.code anthrax_sasp.nuc

from DNASeq import *
from codon_table import *
import sys

if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

codons = codon_table()
codons.read(sys.argv[1])

seq = DNASeq()
seq.read(sys.argv[2])
rc_seq = DNASeq(seq.reverseComplement())

if codons.startswith_init(seq):
    print("Initial codon is a translation start codon")

for frame in (1,2,3):
    print("Frame",frame,"(forward):",codons.translate(seq,frame))
    print("Frame",frame,"(reverse):",codons.translate(rc_seq,frame))
