# BINF6200
# Module 06 Quiz - Question 6
# By Spencer Elliott

# Function that calculates the coverage of paired-end reads
def calculate_coverage(number_of_reads, read_length, genome_length):

    # Multiply the number of reads by 2 for paired-end sequencing
    total_reads = number_of_reads * 2

    # Multiply number of reads by read length to see how many bases are covered
    total_bases = total_reads * read_length

    # Find proportion of the whole genome length that is covered
    return total_bases / genome_length

# Question 6 example: 10 million paired-end reads, each 150 bp long, for a 5 Mbp genome
print("Coverage:", calculate_coverage(10000000, 150, 5000000), "%")
