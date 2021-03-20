#! /usr/bin/env python3
# %%
# set the name of input DNA sequence file
seqfile = 'nad4L.seq.fasta'


# %%
# open the input file, assign to file handle called 'infile'; include file we want to open, how we want to open it --read 'r' or write 'w'
infile = open(seqfile, 'r')

# print (infile) 


# %%
# read the file, by interacting with file handle (infile).  infile.read() to see the file, .rstrip() strips carriage return, linebreak, etc that is at end of file.  Multiple methods applied with repeated .method
dna_sequence = infile.read()


# %%
# close open file.  
infile.close()


# %%
# print the dna sequence.  
# print(dna_sequence)


# %%
# method len() calculates length of a variable or string.  Below we have calculated the length and stored it in seqlen
seqlen = len(dna_sequence)

#print seqlen
print('Sequence length:', seqlen)


# %%
# use method count() to count number of As
# can print immediately or can store in variable, here numA
numA = dna_sequence.count('A')
freqA = numA/seqlen
freqA = "{:.3f}".format(freqA)
print('Freq of A:', freqA)


# %%
# use method count() to count number of As
numC = dna_sequence.count('C')
freqC = numC/seqlen
freqC = "{:.3f}".format(freqC)
print('Freq of C:', freqC)


# %%
# use method count() to count number of Gs
numG = dna_sequence.count('G')
freqG = numG/seqlen
freqG = "{:.3f}".format(freqG)
print('Freq of G:', freqG)


# %%
# use method count() to count number of Ts
numT = dna_sequence.count('T')
freqT = numT/seqlen
freqT = "{:.3f}".format(freqT)
print('Freq of T:', freqT)


# %%
freqGC = float(freqC) + float(freqG)
print('G+C content:' , freqGC )


# %%
allfreq = float (freqA) + float(freqC) + float(freqG) + float(freqT)
print(float(allfreq) == 1)


# %%



