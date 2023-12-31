import gzip
import sys
import math




prox = {}
dis = {}
k = 5
first = 5
last = 5

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		l = line.split()
		start = int(l[1])
		seq = l[-1]
		if start < 200: counts = prox
		elif start > 800: counts = dis
		else: continue
		for i in range(first, len(seq)-k+1, last):
			kmer = seq[i:i+k]
			if kmer not in counts: counts[kmer] = 0
			counts[kmer] += 1
			
proxtotal = sum(prox.values())
distotal = sum(dis.values())

proxfreq = {}
disfreq = {}

for kmer in prox :
	proxfreq[kmer] = prox[kmer]/proxtotal
	disfreq[kmer] = dis[kmer]/distotal

for kmer in prox:
	score = math.log2(proxfreq[kmer]/disfreq[kmer])
	print(kmer, score) 



					
