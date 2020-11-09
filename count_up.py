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
              
              #part 2- the codes are assuming that my_seq = Seq(theseq.txt)

        #I want to get my seq.values, which consists of a single sequence,
        # to identify each nucleotide separately. But I am not able to find
        # appropriate positioning of with.open command. What I plan to do is
        # get the single sequence in a text file and hopefully that way each
        #nucleotide would be read as a separate entry?
              #my code:
              from Bio.Seq import Seq
                    seq = dict(aspairs(f))
                    seq.values() > 'theseq.txt'
                    my_seq = Seq(theseq.txt) # considering that seq.values() are output in theseq.txt and within this txt file, all nucelotides are separate entities
                    #print(my_seq)
                 def split_str(my_seq, chunk, skip_tail=False):
                   lst = []
                     if chunk <= len(my_seq):
                         lst.extend([my_seq[:chunk]])
                         lst.extend(split_str(my_seq[chunk:], chunk, skip_tail))
                     elif not skip_tail and my_seq:
                         lst.extend([my_seq])
                     return lst

                        #print(split_str(my_seq, 3))
                         print(my_seq.count("ATG")) # answer part 2
  
        #another way I was thinking - if I can translate the seq and get peptide seq,
        #I can find the number of Methionines and thus find all start sites for M
        #and thus get no. of genes indirectly, but whole seq being read as a single entry
        #is causing issues
        from Bio.Seq import Seq
        seq = dict(aspairs(f))
        seq.values() > 'theseq.txt'
        my_seq = Seq(theseq.txt)
        #print(my_seq)
            
        pep = my_seq.translate()
        #print(pep)
              print(pep.count("M")) # answer part 2
              
              #part 3 - 
              for my_seq:
              print(my_seq["TAA":"ATG"]) # I intend to find the gene length of gene ending with TAA stop codon (this code doesn't work correctlt though)
              print(my_seq["TAG":"ATG"]) # gene length of genes ending in TAG
              print(my_seq["TGA":"ATG"]) # gene length of genes ending in TGA
              # I am unable to loop the above three commands so as they can function until all genes are counted
              print.total(my_seq["TAA":"ATG"], my_seq["TAG":"ATG"], my_seq["TGA":"ATG"]) # answer part 3
         
              #part 4 - 
              # I do not understand this part. What I could find after opening this file in Notepad was that 
              # it has only one long sequence. I am not sure how can I see if there are different sequences
              
              #part5 - 
              x = my_seq.count()
              y = #result of part 3
              Percentage = (100*(y))/(x)
              print("The Percentage of coding genome is ", Percentage) # answer part 5
              
         
              


