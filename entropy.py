import sys
import math
h = 0
for i in sys.argv[1:]:
	pi = float(i)
	h -= pi * math.log2(pi)
print(f'{h:.3f}')
	


