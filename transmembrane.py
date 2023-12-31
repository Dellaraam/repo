import sys 
import mcb185

def kdave(protein):

	aas = 'IVLFCMAGTSWYPHEQDNKR'
	kds = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, 
	-3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
	totalkd = 0 
	for aa in protein:
		idx = aas.find(aa)
		kd = kds[idx]
		totalkd += kd
	return totalkd/len(protein)
	
def hydrop(seq, thresh, wsize):
	for i in range(len(seq)-wsize+1):
		pep = seq[i:i+wsize]
		k = kdave(pep)
		if k > thresh and 'P' not in pep:
			return True
	return False 

for name, protein in mcb185.read_fasta(sys.argv[1]):
	if hydrop(protein[:30], 2.5, 8) and hydrop(protein[30:], 2.0, 11): 
		print(name)
