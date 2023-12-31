import sys
import random

def overlap(f1, f2):
	start1, end1 = f1
	start2, end2 = f2
	if start2 <= end1 and end2 >= start1: return True
	if end1 >= start2 and end1 <= end2: return True
	return False 
"""
with open(sys.argv[1], 'rt') as fp:
	for line in fp:
		l1 = line.split() 
		n1 = l1[0]
		s1 = int(l1[1])
		e1 = int(l1[2])
		f1 = (n1, s1, e1)
		with open(sys.argv[2], 'rt') as fp2:	
			for line2 in fp2:	
				l2 = line2.split()
				n2 = l2[0]
				s2 = int(l2[1])
				e2 = int(l2[2])
				f2 = (n2, s2, e2)
				if overlap(f1, f2):
					print(f1, f2)				
"""

def features(file):
	chromo = {}
	with open(file) as fp:
		for line in fp:
			l = line.split()
			n = l[0]
			s = int(l[1])
			e = int(l[2])
			if n not in chromo: chromo[n]= []
			chromo[n].append((s, e))
	return chromo
	
f1s = features(sys.argv[1])
f2s = features(sys.argv[2])	

for n in f1s:
	for f1 in f1s[n]:
		for f2 in f2s[n]:
			if overlap(f1, f2):
				print(f1, f2)