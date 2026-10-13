# BINF6200
# Assignment 2 - Question 3
# By Spencer Elliott

seq = "TCAGTCACTCACTCAG"

# Function to determine whether or not a sequence consists of tandem repeats
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

result = is_tandem_repeat(seq)
print(seq, "tandem repeat:", result)
