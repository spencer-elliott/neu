# BINF6200
# Assignment 7 - Question 2
# By Spencer Elliott

# This program fetches a JSON format UniProt entry and prints each reference with some info about it.
# Command line example: python3 q2.py

import urllib.request
import json

# Define the URL
url = 'http://www.uniprot.org/uniprot/Q9H400.json'

# Open the URL and load the JSON data
with urllib.request.urlopen(url) as response:
    data = json.load(response)

# Go through each reference inside the entry
references = data.get('references')
for ref in references:
    # Print the reference number
    print("==== Reference", ref.get('referenceNumber'), "====")
    # Get the citation info
    citation = ref.get('citation')
    # Print citation info
    print("Type:", citation.get('citationType'))
    print("Name:", citation.get('journal'))
    print("Date:", citation.get('publicationDate'))
    print("Volume:", citation.get('volume'))
    print('\n')
