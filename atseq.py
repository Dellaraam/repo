import random
seq = ''
n = 30
at = 0
for i in range(n):
	if random.random() < 0.6: 	
		seq += random.choice('AT') 
		at += 1
	else: 
		seq += random.choice('CG')

print(n, at/n, seq)
