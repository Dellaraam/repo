import mcb185
import sys
import argparse 

	  
def anti(seq):
	antiseq = '' 
	for nt in seq:
		if nt == 'A': antiseq = 'T' + antiseq 
		elif nt == 'T': antiseq = 'A' + antiseq
		elif nt == 'G': antiseq = 'C' + antiseq
		elif nt == 'C': antiseq = 'G' + antiseq 
		else: antiseq = 'N' + antiseq
	return antiseq

def findpeps(seq, strand="+", minorf=100):
	i = 0
	while i < len(seq):
		if seq[i] == 'M':
			start = i
			while i < len(seq):
				if seq[i] == '*':
					end = i 
					if seq[start:end+1] < minorf: continue
					if strand == '+':
						yield start, end, '+', seq[start:end+1]
						break
					else:
						yield len(seq) - end, len(seq) - start, '-', seq[start:end+1]
						break
				i += 1
		i += 1 

for seq in mcb185.read_fasta(sys.argv[1]):
	for f in range(3):
		tseq = mcb185.translate(seq,f)	
		rseq = mcb185.translate(anti(seq),f)
		for start, end, strand, protein in findpeps(tseq, strand='+'):
			print(name, start*3+1, end*3+3, '+', protein[:10])
		for start, end, strand, protein in findpeps(rseq, strand='-'):
			print(name, start*3-3, end*3-1,'-', protein[:10])