# BINF6200
# Assignment 6 - Question 2
# By Spencer Elliott

# This program opens a RefSeq (FASTA) and a SwissProt (XML) sequence record, parses each one, and calculates/compares the amino acid frequencies.
# Command line example: python3 q2.py yeast-ribosome.fasta.gz uniprot_sprot_chunk.xml.gz

import Bio.SeqIO
import gzip
import sys

# Get sequence file names from the command line
seqfilename_fasta = sys.argv[1]
seqfilename_xml = sys.argv[2]

# Function to get a dictionary of amino acid counts
def aa_counts(seqfilename, filetype, mode):
    # Dictionary to store counts of each amino acid
    counts = {}
    # Open the file and iterate through its sequences
    seqfile = gzip.open(seqfilename, mode=mode)
    for seq_record in Bio.SeqIO.parse(seqfile, filetype):
        # Add the amino acids in each record to the count totals (counting every symbol)
        seq = seq_record.seq
        for aa in seq:
            if aa in counts:
                counts[aa] += 1
            else:
                counts[aa] = 1
    # Close the file
    seqfile.close()
    # Return the dictionary of counts
    return counts

# Create a dictionary of amino acid counts for each file
fasta_counts = aa_counts(seqfilename_fasta, "fasta", "rt")
xml_counts = aa_counts(seqfilename_xml, "uniprot-xml", "rb")

# Function to turn the amino acid counts into frequencies
def aa_frequencies(aa_counts):
    frequencies = {}
    total_counts = sum(aa_counts.values())
    for aa in aa_counts:
        frequencies[aa] = aa_counts[aa] / total_counts
    return frequencies

# Turn the amino acid counts into frequencies for each record
fasta_frequencies = aa_frequencies(fasta_counts)
xml_frequencies = aa_frequencies(xml_counts)

# Function to find the highest and lowest frequency amino acids
def aa_comparison(frequencies):
    highest_aa = None
    highest_freq = 0
    lowest_aa = None
    lowest_freq = 1
    # Iterate through the frequencies and keep track of the highest + lowest ones
    for aa in frequencies:
        if frequencies[aa] > highest_freq:
            highest_aa = aa
            highest_freq = frequencies[aa]
        elif frequencies[aa] < lowest_freq:
            lowest_aa = aa
            lowest_freq = frequencies[aa]
    return highest_aa, lowest_aa

# Function to find amino acids with the greatest differences in frequency between the two files
def difference_comparison(fasta_frequencies, xml_frequencies):
    # Create a dictionary to hold differences
    differences = {}
    # Iterate through the frequency lists and find the difference for each amino acid
    for aa in fasta_frequencies:
        if aa in xml_frequencies:
            differences[aa] = abs(fasta_frequencies[aa] - xml_frequencies[aa])
    # Sort the dictionary from highest to lowest difference
    ranked = sorted(differences, key=differences.get, reverse=True)
    # Return info on the 3 amino acids with the greatest differences
    greatest_differences = []
    for aa in ranked[0:3]:
        greatest_differences.append((aa, differences[aa]))
    return greatest_differences

# Find the most and least frequent amino acids in the RefSeq file, and print results
fasta_comparison = aa_comparison(fasta_frequencies)
print("Most common amino acid in RefSeq:", fasta_comparison[0])
print("Least common amino acid in RefSeq", fasta_comparison[1])

# Find the most and least frequent amino acids in the SwissProt file, and print results
xml_comparison = aa_comparison(xml_frequencies)
print("Most common amino acid in SwissProt:", xml_comparison[0])
print("Least common amino acid in SwissProt", xml_comparison[1])

# Find the 3 amino acids with the greatest difference in frequency between the two files, and print results
greatest_differences = difference_comparison(fasta_frequencies, xml_frequencies)
print("\nAmino acids with the biggest differences in frequency:")
for aa, diff in greatest_differences:
    print(str(aa) + ": " + str(diff))
