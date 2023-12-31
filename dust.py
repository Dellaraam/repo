#!/usr/bin/env python3
import mcb185
import sys
import math
import argparse 



def ntp(seq):
	a = 0
	c = 0
	g = 0
	t = 0
	for nt in seq:
		if nt == 'A':
			a += 1
		elif nt == 'C':
			c += 1
		elif nt == 'G':
			g += 1
		elif nt == 'T':
			t += 1
	total = a+c+g+t
	return a/total, c/total, g/total, t/total	
		

def entropy(probs):
	h = 0
	for pi in probs:
		if pi == 0: continue 
		h -= pi * math.log2(pi)
	return h
		
def mask(seq, w, t, lc):
	out = list(seq)
	for i in range(len(seq)-w+1):
		if entropy(ntp(seq[i:i+w])) < t:
			for j in range(i,i+w):
				if lc:
					out[j] = seq[j].lower()
				else:
					out[j] = 'N'
	return ''.join(out)			


		
parser = argparse.ArgumentParser(description='Adds options and default')
parser.add_argument('file', type=str, help='fasta file')
parser.add_argument('--ws', required=False, type=int, default= 11,
	metavar='<int>', help='optional inatger argument [%(default)s]')
parser.add_argument('--th', required=False, type=int, default= 1, 
	metavar='<int>', help='optional inatger argument [%(default)s]')
parser.add_argument('--lse', action='store_true',
	help='N-base or lowercase')
arg = parser.parse_args()




for name, seq in mcb185.read_fasta(arg.file):
	print(f'>{name}')
	seq = mask(seq, arg.ws, arg.th, arg.lse)
	for i in range(0,len(seq),60):
		print(seq[i:i+60])














