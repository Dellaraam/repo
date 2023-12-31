import gzip
import sys


# init: create empty counts 
aas = 'ACDEFGHIKLMNPQRSTVWY' 
counts = []
total = 0
for i in range(len(aas)):
	counts.append(0)

#count every amino acid in the file 	
fp = gzip.open(sys.argv[1], 'rt') 
for line in fp: 
	if line.startswith('>'): continue 
	line = line.rstrip()
	for aa in line:
		idx = aas.find(aa)
		counts[idx] += 1
		total +=1

	
		

#termination print output  
for aa, n in zip(aas, counts):
	print(aa, n, n/total)	

"""
fp = gzip.open(sys.argv[1], 'rt') 		
def composition(aa): 

	A = 0
	C = 0
	D = 0 
	E = 0
	F = 0
	G = 0 
	H = 0
	I = 0
	K = 0 
	L = 0
	N = 0
	M = 0
	P = 0
	Q = 0
	R = 0
	S = 0
	T = 0
	V = 0
	W = 0
	Y = 0
	for line in fp:
		if line.startswith('>'): continue 
		for aa in line:
			if aa == 'A': A += 1
			elif aa == 'C': C += 1
			elif aa == 'D': D += 1 
			elif aa == 'E': E += 1
			elif aa == 'F': F += 1
			elif aa == 'G': G += 1
			elif aa == 'H': H += 1
			elif aa == 'I': I += 1
			elif aa == 'K': K += 1
			elif aa == 'L': L += 1
			elif aa == 'N': N += 1
			elif aa == 'M': M += 1
			elif aa == 'P': P += 1
			elif aa == 'Q': Q += 1
			elif aa == 'R': R += 1
			elif aa == 'S': S += 1
			elif aa == 'T': T += 1
			elif aa == 'V': V += 1
			elif aa == 'W': W += 1
			elif aa == 'Y': Y += 1
	return A, C, D, E, F , G, H, I, K, L, M ,N, P, Q, R, S ,T, V, W, Y 

print(composition(fp), composition(fp)/len(aa))
"""