alph = 'ARNDCEQGHILKMFPSTWYV'
combo = 0 
for i in range(0,len(alph)):
	for j in range(1+i,len(alph)):
		print(alph[i],alph[j])
		combo += 1
print(combo)