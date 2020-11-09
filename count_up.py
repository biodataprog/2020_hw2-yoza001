#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

#gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re,Bio,textwrap

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence




#if not os.path.exists(gff):
 #   os.system("curl -L -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_subst$

if not os.path.exists(fasta):
    os.system("curl -L -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_s$

#print ("filename is {}".format(filename))
with gzip.open(fasta,"rt") as f:
    # now add code to process
#       print("filename is {}".format(f))
        #I want to get my seq.values, which consists of a single sequence,
        # to identify each nucleotide separately. But I am not able to find
        # appropriate positioning of with.open command. What I plan to do is
        # get the single sequence in a text file and hopefully that way each
        #nucleotide would be read as a separate entry?
  
        #another way I was thinking - if I can translate the seq and get peptide seq,
        #I can find the number of Methionines and thus find all start sites for M
        #and thus get no. of genes indirectly, but whole seq being read as a single entry
        #is causing issues
        from Bio.Seq import Seq
        seq = dict(aspairs(f))
        seq.values() > 'theseq.txt'
        my_seq = (seq.values())
        #print(my_seq)
#       def split_str(my_seq, chunk, skip_tail=False):
#           lst = []
#           if chunk <= len(my_seq):
#               lst.extend([my_seq[:chunk]])
#               lst.extend(split_str(my_seq[chunk:], chunk, skip_tail))
#           elif not skip_tail and my_seq:
#               lst.extend([my_seq])
#           return lst


#       print(split_str(my_seq, 3))
#       codon = [split_str(my_seq, 3)]
#       print(len(codon))
              
 #print textwrap.wrap(my_seq, 3)
        #print(my_seq)
        #pep = my_seq.translate()
        #print(pep)
#with gzip.open(gff,"rt") as f:
#       seq = dict(aspairs(f))
#       first_codon_count = 0
#       atg_blank = {}
#       i = 0
#       for seqname in seq:


#print(seq)



