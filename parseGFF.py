#! /usr/bin/env python3
# if get "bad interpreter" error, problem likely with shebang above

import csv
# import csv module / package to parse in tab delimited or csv file
# import statements go at VERY TOP
import argparse 
# import argparse to accept and parses command line arguments
# import Bio # import Biopython (only works if Biopython is installed)
from Bio import SeqIO # import SeqIO from Biopython, use this because Biopython is a BIG package, so import part we need instead of whole package

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
print('The genome id is', genome.id)
print('The length of the genome sequence is', len(genome.seq)) # from looking in genome, see that sequence is held as genome.seq
print()
#print(genome.seq) #prints the whole genome sequence


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
        geneid = line[8]
        # print('This gene is', geneid)
        #print('The start coordinate is', line[3], ', the end coordinate is', line[4], ', and the strand is', line[6]) # print field 3 and 4 of line
        
        # print genome.id from genome object and geneid from reader object
        print('>' + genome.id, geneid)
        
        # print start and end coordinate and strand for each line
        # print('The start coordinate is', line[3], ', the end coordinate is', line[4], ', and the strand is', line[6]) # print field 3 and 4 of line
        
        # extract and print nucleotide sequence region from genome.seq, sliced by startcoord-1 and endcoord made into integers, because slicing requires integers
        # used startcoord-1 for start coordinate, because of zero indexing, start at base pair 1 was start at index 0
        # did not adjust end coordinate because the -1 from zero indexing offsets the fact that the slice end location is not included
        # print(genome.seq[int(startcoord)-1:int(endcoord)]) #<-- this works, but doesn't acount for strand

        # must account for strand
        # if strand is plus, print indicated sequence
        if strand == '+':
            print(genome.seq[int(startcoord)-1:int(endcoord)])

        # if strand is minus, find indicated sequence THEN take reverse complement.
        # Doing genome.seq.reverse_complement()[index numbers] chooses the range after doing the reverse complement and this doesn't give the correct gene
        # Found .reverse_complement() at https://biopython.org/wiki/Seq
        else:
            print(genome.seq[int(startcoord)-1:int(endcoord)].reverse_complement())