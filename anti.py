dna = 'ACTGAAAAAAAAAAA'
anti = ''
for nt in dna:
	if   nt == 'A': anti = 'T' + anti 
	elif nt == 'C': anti = 'G' + anti
	elif nt == 'G': anti = 'C' + anti
	elif nt == 'T': anti = 'A' + anti
	
print(anti)
	
