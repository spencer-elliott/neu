# Testing assignment 8 modules here

import sys
from MyDNAStuff import read_seq_from_filename
from MyDNAStuff import complement
from MyDNAStuff import reverseComplement

seqfilename = sys.argv[1]

seq = read_seq_from_filename(seqfilename)
cseq = complement(seq)
rcseq = reverseComplement(seq)

print(" Sequence:",seq)
print(" C sequence:",cseq)
print("RC sequence:",rcseq)
