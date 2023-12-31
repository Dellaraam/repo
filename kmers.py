import argparse 
import sys 
import random
import mcb185


def kmers(seq, k):
	kcount = {}

	for i in range(len(seq)-k+1):
		kmer = seq[i:i+k]
		if kmer not in kcount:
			kcount[kmer] = 0
		kcount[kmer] += 1
	return kcount

parser = argparse.ArgumentParser(description='changes frame')
parser.add_argument('file', type=str, help='fasta file')
parser.add_argument('--k', required=False, type=int, default= 2,
	metavar='<int>', help='optional inatger argument [%(default)s]')
arg = parser.parse_args()
	
for name, seq in mcb185.read_fasta(arg.file):
	print(kmers(seq, arg.k))
	
		
			
	
		
		