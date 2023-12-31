dna = 'GTGAGTTTTCGAATGTGAGTTCCCAAGCACTTATATATGTTTTAG'

for i in range(0, len(dna)-2, 3): #len(dna)-4 also works 
	print(dna[i:i+3])
#for i in range(len(dna)):
	#codon = dna[i:i+3]
	#print(codon)
	
k = 5
for i in range(len(dna)-k+1):
	print(dna[i:i+k])

#why does -2 have to be there? something about not running over?	

		