# BINF6200
# Assignment 8 - Question 1
# By Spencer Elliott

# Translates an amino-acid sequence in all six-frames, using the codon_table.py module
# Usage example: python3 q1.py standard.code anthrax_sasp.nuc

from MyDNAStuff import *
from codon_table import *
import sys

if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

table = read_codons_from_filename(sys.argv[1])
seq = read_seq_from_filename(sys.argv[2])
rc_seq = reverseComplement(seq)

if is_init(table,seq[:3]):
    print("Initial codon is a translation start codon")

for frame in (1,2,3):
    print("Frame",frame,"(forward):",translate(table,seq,frame))
    print("Frame",frame,"(reverse):",translate(table,rc_seq,frame))
