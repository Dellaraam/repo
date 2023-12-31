import re
import argparse 
import gzip
import sys 

def rc(seq):
	nseq = '' 
	for nt in seq[::-1]:
		if nt == 'a': nseq += 't' 
		elif nt == 't': nseq += 'a'
		elif nt == 'g': nseq += 'c' 
		elif nt == 'c': nseq += 'g' 
		else: nseq += 'N' 
	return nseq
#get sequence 
genome = ''
with gzip.open(sys.argv[1], 'rt') as fp :
	for line in fp:
		if line.startswith('ORIGIN'): break
	for line in fp:
		f = line.split()
		seq = ''.join(f[1:])
		genome += seq

#get the CDS's 
with gzip.open(sys.argv[1], 'rt') as fp :
	starts = {}
	for line in fp:
		if line.startswith('     CDS'):
			m = re.search('(\d+)\.\.(\d+)', line)
			if m:
				start = int(m.group(1)) -1
				end = int(m.group(2)) -1
			if 'complement' in line: strand = '-'
			else: strand = '+'
				
			if 'join' in line: continue
			start_codon = None 
			if strand == '+':
				start_codon = genome[start:start+3]
			else: 
				rcstart = genome[end-2:end+1]
				start_codon = rc(rcstart)
			
			if start_codon not in starts: starts[start_codon] = 0
			starts[start_codon] += 1
			
			
for codon, n in starts.items():
	print(codon, n, strand)	