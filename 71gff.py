import sys
import json
import gzip
import re


with gzip.open(sys.argv[1], 'rt') as fp:
	genome = {}
	counts = {}
	i = []
	eyes = 0
	ii = []
	iis = 0
	iii = []
	iiis = 0
	iv = []
	ivs = 0
	mtd = []
	mtds = 0
	v = []
	vs = 0
	x = []
	xs = 0
	for line in fp:
		c = line.split()
		if c[2] == 'gene':
			m = re.search('name=(\S+?);', c[8])
			n = m.group(1)
			b = int(c[3])
			e = int(c[4])
			s = c[6]
			if c[0] == 'I':
				i.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['I'] = i
				eyes += 1
			if c[0] == 'II':
				ii.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['II'] = ii
				iis += 1
			if c[0] == 'III':
				iii.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['III'] = iii
				iiis += 1
			if c[0] == 'IV':
				iv.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['IV'] = iv
				ivs += 1
			if c[0] == 'MtDNA':
				mtd.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['MtDNA'] = mtd
				mtds += 1
			if c[0] == 'V':
				v.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['V'] = v
				vs += 1
			if c[0] == 'X':
				x.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
				genome['X'] = x
				xs += 1
	print('I', eyes, 'II', iis, 'III', iiis,'IV', ivs, 'MtDNA', mtds, 'V', vs, 'X', xs)
	print(json.dumps(genome, indent=4))						

