from statistics import *
fil = open("93cars.dat.txt")

def work():
	c = []
	h = []
	m = []
	for i in range(186):
		line = fil.readline()
		if(len(line) > 44):
			x = int(line[52:54])
			y = int(line[55:57])
			z = float(line[42:46])
			c.append(x)
			h.append(y)
			m.append(z)
	print("Average city MPG:",mean(c))
	print("Average highway MPG:",mean(h))
	print("Average midrange prices:",mean(m))

work()
