#! /usr/bin/env python3

# script goal: read in GFF file and get begin and end coordinates; go into genome and extract that sequence

# import needed modules; import statements go at beginning of script
# import csv module / package to parse in tab delimited or csv file
import csv
# import argparse to accept and parse command line arguments
import argparse 
# import SeqIO from Biopython, use this because Biopython is a BIG package, so import part we need instead of whole package as import Bio
from Bio import SeqIO 
# import default dictionary module to create and use dictionaries
from collections import defaultdict
# import re to use regular expressions
import re


# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')
# description is optional, but useful

# add positional arguments (positional because **order matters**)
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument('fasta', help='name of the FASTA file')

# parse the arguments.  Give to object args, which holds values=arguments from parsed command line entry
args = parser.parse_args()


# open and read in FASTA file, assign to genome object
# plan to access resulting genome.seq with info from GFF, thus open and read in FASTA before GFF, so that genome.seq is available to GFF
genome = SeqIO.read(args.fasta, 'fasta') #SeqIO dot read method (filename, type of file)
# print(genome) # to see what is held in genome object, see http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec32
print('The genome id is', genome.id)
print('The length of the genome sequence is', len(genome.seq)) # from looking in genome, see that sequence is held as genome.seq
#print(genome.seq) #prints the whole genome sequence


# create a nested dictionary called CDS_dict with gene name as outer key, exon number as inner key and 'CDS_coords' list  as value
CDS_dict = defaultdict(dict)


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
               
        # skip empty lines and label fields in non-empty lines
        # skip empty lines
        if not line :
            continue

        # for non-empty lines assign fields to variable names, using zero indexing, [#] is [index]
        else :
            genus = line[0].split()[0]
            species = line[0].split()[1]
            feature = line[2]
            startcoord = str(int(line[3])-1) # need startcoord = start-1, because of zero indexing, start at base pair 1 was start at index 0
            endcoord = line[4] # do not adjust endcoord because the -1 from zero indexing offsets the fact that the slice end location is not included
            strand = line[6]
            attributes = line[8].split(sep=";") # splits attributes string into a list at the semicolons
            line[-1] = attributes # replaces previous attributes string field with a list
            attrib_str = str(attributes) # convert attributes list into a string

        # skip non-CDS lines and extract gene name and exon number from CDS lines
        # skip lines that are not CDS features
        if feature != 'CDS':
            continue
        
        # for lines that are CDS features, parse attributes for gene name and exon number
        else:
            match = re.search('Gene\s(\S+)\s(\S+)?\s?(\d+)?', attrib_str)
            gene_name = match.group(1)
            exon_number = match.group(3)
            # gene_exon = gene_name + '-' + str(exon_number)


        # create CDS_coords list with strand and start and end coordinates, to act as values in CDS_dict
        CDS_coords = [strand, startcoord, endcoord]

        # populate CDS_dict with outer key [gene_name], inner key [exon number] and value CDS_coords list
        CDS_dict[gene_name][exon_number] = CDS_coords
        #print(CDS_dict)

        # create sort_dict function to sort by outer and inner dictionary keys (copied from https://gist.github.com/gyli/f60f0374defc383aa098d44cfbd318eb)
        def sort_dict(item: dict): 
            return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}

# use sort_dict function to sort CDS_dict by outer key (gene name), then inner key (exon number) and assign to sorted_CDS_dict
sorted_CDS_dict = sort_dict(CDS_dict)


# convert sorted_CDS_dict to list for better access
sorted_CDS_list = list(sorted_CDS_dict.items())


# loop through list and print header with gene name and sequence
for i in sorted_CDS_list :
    gene = i[0] # gene name is first list item
    # print(gene)
    gene_dict = i[1] # second list item is dictionary of gene elements; key is exon number, value is list of strand, startcoord, end coord
    # print(gene_dict)
    concat_seq = '' # resets concat_seq to blank for each gene name; prevents one gene bleeding into another

    for n, m in gene_dict.items(): # sets first (n) to key, second (m) to value
        exon_number = n
        #print(exon_number)
        strand = m[0]
        #print(strand)
        start = m[1]
        #print('start', start)
        end = m[2]
        #print('end', end)
           
        # if strand is plus, find and store indicated sequence
        if strand == '+':
            seq_content = genome.seq[int(start):int(end)]
            concat_seq += seq_content # add new sequence content to existing
            
        # if strand is minus, find indicated sequence THEN take reverse complement and store that
        else:
            seq_content=genome.seq[int(start):int(end)].reverse_complement()
            concat_seq += seq_content # add new sequence content to existing

    print('>' + genus + "_" + species + "_" + gene) # print header
    print(concat_seq) # print concatenated exon sequence
    print()

    

