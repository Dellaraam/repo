import sys
import json
import gzip
import re


with gzip.open(sys.argv[1], 'rt') as fp:
	genes = []
	for line in fp:
		if line.startswith('#'): continue
		c = line.split()
		if c[2] == 'gene':
			m = re.search('Name=(\S+?);', c[8])
			n = m.group(1)
			b = int(c[3])
			e = int(c[4])
			s = c[6]
			genes.append({'gene': n, 'beg': b, 'end': e, 'strand': s})
print(json.dumps(genes, indent=4))		
		
		
		
		
"""		
with open(sys.argv[1]) as fp:
	course = json.load(fp)

print(course)
course['Students'][0]['Name'] = "Chanel"
course['Students'].append({"Name": 'Jason', 'Year': '1'})
print(json.dumps(course, indent=4))
"""




		
		