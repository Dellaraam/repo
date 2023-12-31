import sys
import math

#get the data 
vals = []
for i in sys.argv[1:]:
	vals.append(float(i))
#calculate stuff
count = len(vals)
min = vals[0]
max = vals[0]
total = vals[0]
for val in vals[1:]:
	if val < min:
		min = val
	if val > max:
		max = val
	total += val
mean = total/count
vals.sort()
median = None
mid = len(vals)//2
if len(vals) % 2 != 0:
	median = len(vals)//2
else: 
	median = (vals[mid] + vals[mid-1])//2 
var = 0 
for va in vals:
	var += (va - mean)**2/count
std = math.sqrt(var)
#output stuff
print("count:", count)
print("Minimum:", min)
print("Maximum:", max )
print("Mean:", mean)
print("Median:", median)
print("Std:", std)

