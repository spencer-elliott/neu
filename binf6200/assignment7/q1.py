# BINF6200
# Assignment 7 - Question 1
# By Spencer Elliott

# This program fetches an XML format UniProt entry and prints each reference with some info about it.
# Command line example: python3 q1.py

import xml.etree.ElementTree as ET
import urllib.request

# Fetch the XML formatted entry
thefile = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q9H400.xml')
# Parse the entry
document = ET.parse(thefile)
# Access the root node
root = document.getroot()

# Namespace to precede each tag
ns = '{http://uniprot.org/uniprot}'

# Start by getting the entry 
entry = root.find(ns+'entry')
# Go through each reference inside the entry
for ref in entry.findall(ns+'reference'):
    # Print the reference number
    print("==== Reference", ref.attrib['key'], "====")
    # Get the citation info
    citation = ref.find(ns+'citation')
    # Print citation info
    print("Type:", citation.get('type'))
    print("Name:", citation.get('name'))
    print("Date:", citation.get('date'))
    print("Volume:", citation.get('volume'))
    print("\n")
