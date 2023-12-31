#objects that contain the sequence abd how mant base pairs we need 
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

#loop that perses through the range of letters 
for i in range(len(seq)-w+1):
	#store the window and amount of G's anf C's 
	win = seq[i:i+w] 
	gc = 0
	#check every nucleotide in the window and count G and C
	for nt in win:
		if nt == 'C' or nt == 'G': gc +=1
	print(i,win,gc/w)