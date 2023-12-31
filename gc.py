dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
gc = 0
for i in range(len(dna)):
	if dna[i] == 'G' or dna[i] == 'C': gc += 1/len(dna)
		
print(f'{gc:.2f}')
