# BINF6200
# Assignment 6 - Question 1
# By Spencer Elliott

# This file reads a microarray data file, and finds the mean and standard deviation for expression of a specific gene.
# Command line example: python3 q1.py data.csv N40554

import sys
import csv
import math

# Take file name and gene name as command-line arguments
data_file = open(sys.argv[1])
gene_name = sys.argv[2]

# Create a dictionary from the csv file
rows = csv.DictReader(data_file)

# Extract the category and value in each row for the target gene
categories = []
values = []
for r in rows:
    categories.append(r["TUMOUR"])
    values.append(float(r[gene_name]))

# Close the file
data_file.close()

# Sort values into categories 1 and 2
category1_values = []
category2_values = []
for i in range(len(values)):
    if categories[i] == "1":
        category1_values.append(values[i])
    elif categories[i] == "2":
        category2_values.append(values[i])
    else:
        pass

# Function to calculate the mean of a list of values
def mean(values):
    return sum(values) / len(values)

# Function to calculate the standard deviation of a list of values
def standard_deviation(values):
    total_squared_distance = 0
    m = mean(values)
    for v in values:
        total_squared_distance += (v - m) ** 2
    standard_deviation = math.sqrt(total_squared_distance / len(values))
    return standard_deviation

# Print results
print("Overall Mean:", mean(values))
print("Overall Standard Deviation:", standard_deviation(values))
print("Category 1 - Mean:", mean(category1_values), ", Standard Deviation:", standard_deviation(category1_values))
print("Category 2 - Mean:", mean(category2_values), ", Standard Deviation:", standard_deviation(category2_values))
