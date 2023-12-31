import sys
import argparse 
import mcb185

imeter = {}
with open('imetertrained5') as fp:	
	for line in fp:
		kmer, score = line.split()	
		imeter[kmer] = float(score) 
first = 5
last = 10
k = 5
for name, seq in mcb185.read_fasta(sys.argv[1]):
	intronscore = 0
	for i in range(first, len(seq)-k - last + 1):
		kmer = seq[i:i+k]
		if kmer in imeter:
			intronscore += imeter[kmer]
	print(name, intronscore)	
				
				
				
# I have a list of all possible kmers 
# I get kmers from the file of introns given 
# If a kmer exists in the list of all possible kmers 
# Add the .values() together to see the total intron score 
# If the intron score is positive then the intron is probably proximal to the start codon






