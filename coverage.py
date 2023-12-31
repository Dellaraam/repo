import sys
import random


gsize = int(sys.argv[1])
rl = int(sys.argv[2])
rn = int(sys.argv[3])
genome = [0] * gsize #creat genome
for i in range(rn):
	beg = random.randint(0, gsize - rl) #list of reads 
	for j in range(beg, beg+rl): 
	#compare 
		genome[j] += 1
print(min(genome[rl:-rl]))
print(max(genome[rl:-rl]))
print(genome[rl:-rl]/rn)

#i assume that the sequences pile on each-other randomly?
#counts read number 
#need somthing that looks at possibilities of numbers covering other numbers


	