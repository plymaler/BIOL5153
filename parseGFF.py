#! /usr/bin/env python3
# if get "bad interpreter" error, problem likely with shebang above

import csv
# import csv module / package to parse in tab delimited or csv file
# import statements go at VERY TOP
import argparse 
# import argparse to accept and parses command line arguments
# import Bio # import Biopython (only works if Biopython is installed)
from Bio import SeqIO # import SeqIO from Biopython, use this becuase Biopython is a BIG package, so import part we need instead of whole package

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)
# read in GFF file and get begin and end coordinates; go into genome and extract that sequence

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')
# description is optional, but useful

# add positional arguments (positional because **order matters**)
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument('fasta', help='name of the FASTA file')

# parse the arguments.  Give to object args, which holds values=arguments from parsed command line entry
args = parser.parse_args()

# print(args.gff)
# to confirm gff filename

# open and read in FASTA file, assign to genome object
genome = SeqIO.read(args.fasta, 'fasta') #SeqIO dot read method (filename, type of file)
#print(genome) # to see what is held in genome object, see http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec32
print(genome.id)
print(len(genome.seq)) # from looking in genome, see that sequence is held as genome.seq
print(genome.seq)


# open and read in GFF file, retrieve gff from args object using dot notation
with open(args.gff, 'r') as gff_in:
    # create a csv reader object, which is A LIST
    reader = csv.reader(gff_in, delimiter='\t')
    # use variable/object name reader, call csv package with reader method and specify imput and delimiter.
    # parse gff file using tab delimiter
    # change delimiter to , to use on csv file.  can put in any one character delimiter
    # now use reader object to access data

    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        # assign fields to variable names, using zero indexing, [#] is [index]
        startcoord = line[3]
        endcoord = line[4]
        strand = line[6]
        #print(startcoord)
        #print(line[3], line[4]) # print field 3 and 4 of line

        # extract the sequence (must already have opened and parsed FASTA file to use genome.seq here)
# take a slice out of a string -> take start and end coordinates and strand and use those to extract that fragment of DNA from the genome.
