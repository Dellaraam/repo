dna = 'ATGGCCTTT'

for i in range(0,len(dna),3):
	for j in range(3):
		print(i+j,j,dna[i+j])

for l in range(len(dna)):
	nt = dna[l]
	print(l,l%3,nt)