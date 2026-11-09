# BINF6200
# Assignment 8 - Question 1 - Module with nucleotide functions
# By Spencer Elliott

# Function to read in a sequence from a file
def read_seq_from_filename(seq_filename):
    seq_file = open(seq_filename)
    dna_seq = ''.join(seq_file.read().split())
    dna_seq = dna_seq.upper()
    seq_file.close()
    return dna_seq

compl_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

# Function to find the complement of a sequence (Lecture 8)
def complement(seq):
    return ''.join(map(compl_dict.get,seq))

# Function to reverse a sequence (Lecture 8)
def revseq(seq):
    return ''.join(reversed(seq))

# Function to find the reverse complement of a sequence (Lecture 8)
def reverseComplement(seq):
    return complement(revseq(seq))

# Assignment 1, Question 1: Print a codon backwards and in lower case
def reverse_lowercase_codon(codon):
    # Use negative string indexing to print characters in reverse
    codon_reverse = codon[-1] + codon[-2] + codon[-3]
    # Return as lowercase with the .lower() method
    return(codon_reverse.lower())

# Assignment 1, Question 2: Find the first start codon position and translation frame for a sequence
def start_codon_info(sequence):
    # Ensure the sequence is all upper case
    sequence_upper_case = sequence.upper()
    # Find the position of start codon
    start_position = sequence_upper_case.find("ATG")
    # Find the translation frame as the remainder when divided by 3
    # String indexing starts at 0, so we need to add 1 first
    translation_frame = (start_position % 3) + 1
    return(start_position, translation_frame)

# Assignment 2, Question 1: Find various information about a sequence
def sequence_info(sequence):
    # Ensure the sequence is all upper case
    seq_upper = sequence.upper()
    # Check if the sequence starts with a Met codon
    starts_with_met = seq_upper.startswith("ATG")

    # Check if the sequence has a frame 1 Met codon
    # Iterate through each codon in frame 1, and check if it is ATG
    frame_1_met = False
    for i in range(0, len(seq), 3):
        if seq_upper[i:i+3] == "ATG":
            frame_1_met = True
    
    # Count how many nucleotides are in the gene
    number_of_nucleotides = len(seq_upper)
    # Count how many amino acids are in the protein (number of codons)
    # The whole sequence will be translated, so this is just length / 3
    number_of_amino_acids = int(len(seq_upper) / 3)

    # Calculate the G/C content
    g_count = seq_upper.count("G")
    c_count = seq_upper.count("C")
    gc_content = ((g_count + c_count) / number_of_nucleotides) * 100
    # Round to two decimal places
    gc_content = round(gc_content, 2)

    # Return all the information
    return(starts_with_met, frame_1_met, number_of_nucleotides, number_of_amino_acids, gc_content)

# Assignment 2, Question 2: Find the reverse complement of a codon
def reverse_complement_codon(codon):
    # First, reverse the codon
    codon_reverse = codon[::-1]
    # Then each nucleotide in the codon becomes its complement
    reverse_complement = ""
    for i in range(3):
        reverse_complement += complement(codon_reverse[i])
    return reverse_complement

# Assignment 2, Question 3: Determine whether or not a sequence is made up of tandem repeats
def is_tandem_repeat(seq):
    seq_length = len(seq)
    # Check through every possible length for a repeat (From 1 to half of the sequence length)
    for repeat_length in range(1, seq_length // 2 + 1):
        # The repeat length has to divide evenly into the sequence (remainder == 0)
        if seq_length % repeat_length == 0:
            repeat = seq[0:repeat_length]
            number_of_repeats = seq_length // repeat_length
            # Test this tandem repeat by trying to build the same sequence
            if repeat * number_of_repeats == seq:
                return True
    # If no tandem repeats were found, return False
    return False

# Assignment 3, Question 2: Function to check if a sequence is a reverse compliment palindrome
def isPalindrome(seq):
    reverse_comp = reverseComplement(seq)
    # Compare the sequence against its reverse complement
    if seq.upper() == reverse_comp:
        return True
    else:
        return False
