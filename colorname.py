import sys

colors = { 
	'red': (255, 0,0),
	'green': (0, 255, 0),
	'blue': (0, 0, 255),
	'cyan': (0, 255, 255),
	'yellow': (255, 255, 0),
	'megenta': (255, 255, 0),
	'white': (0, 0, 0),
}

c = sys.argv[1]  

r = int(c[0:2], 16)
g = int(c[2:4], 16)
b = int(c[4:6], 16)
	
mindist = 255 + 255 + 255
micolor = None

inc = (r, g ,b)

for name, colors in colors.items():
	d = abs(inc[0] - colors[0]) + abs(inc[1] - colors[1]) + abs(inc[2] - colors[2])
	if d < mindist:
		mindist = d
		mincolor = name
print(mincolor)		



	

	 
	





