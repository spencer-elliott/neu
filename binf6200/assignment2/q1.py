# BINF6200
# Assignment 2 - Question 1
# By Spencer Elliott

seq = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"

# Ensure the sequence is all upper case
seq_upper = seq.upper()

# Check if the sequence starts with a Met codon
starts_with_met = seq_upper.startswith("ATG")

# Check if the sequence has a frame 1 Met codon
# Iterate through each codon in frame 1, and check if it is ATG
frame_1_met = False
for i in range(0, len(seq), 3):
    if seq[i:i+3] == "ATG":
        frame_1_met = True

# Count how many nucleotides are in the gene
number_of_nucleotides = len(seq)

# Count how many amino acids are in the protein (number of codons)
# The whole sequence will be translated, so this is just length / 3
number_of_amino_acids = len(seq) / 3

# Calculate the G/C content
g_count = seq.count("G")
c_count = seq.count("C")
gc_content = ((g_count + c_count) / number_of_nucleotides) * 100
# Round to two decimal places
gc_content = round(gc_content, 2)

print("Starts with a Met codon:", starts_with_met)
print("Has a frame 1 Met codon:", frame_1_met)
print("Number of nucleotides:", number_of_nucleotides)
print("Number of amino acids:", int(number_of_amino_acids))
print("G/C content: " + str(gc_content) + "%")
