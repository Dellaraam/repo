import sys

seq1 = 'ACTGTC' #X
seq2 = 'ACGTCT' #Y

match = int(sys.argv[1])
mismatch = int(sys.argv[2])
gap = int(sys.argv[3])

def makematrix(cols, rows, inital):
	mat1 = []
	for i in range(rows):
		vec = []
		for j in range(cols):
			vec.append(inital)
		mat1.append(vec)
	return mat1


def showmat(m, seq1, seq2):
	for col in range(len(seq1)+1): 
		if col == 0:
			print(end='\t')
		else:
			print('\t', seq1[col-1], sep='', end='')
	print()
	for row in range(len(seq2)+1):
		if row == 0: 
			print(end='\t')
		else: 
			print(seq2[row-1], end='\t')
		for col in range(len(seq1)+1):
			print(m[row][col], end='\t')
		print()
		
m1 = makematrix(len(seq1)+1, len(seq2)+1, 0)
m2 = makematrix(len(seq1)+1, len(seq2)+1, '.')

#initialize 	
for i in range(len(seq1)+1): 
	m1[i][0] -= i
for i in range(len(seq2)+1):
	m1[0][i] -= i
showmat(m1, seq1, seq2)

#fill matrix 
gmax = 0
maxrow = None
maxcol = None
for row in range(1, len(seq2)+1):
	for col in range(1, len(seq1)+1): 
		left = m1[row][col-1] + gap 
		top = m1[row-1][col] + gap 
		if seq2[row-1] == seq1[col-1]:
			# assign diagonal and add match value 
			diag = m1[row-1][col-1] + match
		else:
		 	# assign diagonal and add mismatch value(subtract)
		 	diag = m1[row-1][col-1] + mismatch
		#print(left, top, diag, row, col)
		if diag >= top and diag >= left and diag > 0:
			m1[row][col] = diag 
			m2[row][col] = 'd'
			if diag > gmax:
				gmax = diag
				maxrow = row 
				maxcol = col 
				
		elif top >= left and top > 0:
			m1[row][col] = top
			m2[row][col] = 'v'

		elif left > 0:
			m1[row][col] = left
			m2[row][col] = 'h' 
				
		else: 
			m1[row][col] = 0
			m2[row][col] = '.'
			
		#best alignment 
		#if gmax recorded print alignment 
		#if gap print '-'
		
showmat(m1, seq1, seq2)
showmat(m2, seq1, seq2)
print(gmax, maxrow, maxcol)
a1 = ''
a2 = ''
while m2[maxrow][maxcol] != '.':
	if m2[maxrow][maxcol] == 'd':
		a1 += seq1[maxcol-1] 
		a2 += seq2[maxrow-1] 
		maxrow -= 1
		maxcol -= 1
	elif m2[maxrow][maxcol] == 'h':
		a1 += seq1[maxcol-1] 
		a2 += '-'
		maxcol -= 1
	elif m2[maxrow][maxcol] == 'v':
		a1 += '-'
		a2 += seq2[maxrow-1]
		maxrow -= 1
print(a1)
print(a2)



		 		
		 		
		

