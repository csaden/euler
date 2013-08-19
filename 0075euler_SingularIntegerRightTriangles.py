# It turns out that 12 cm is the smallest length of wire that
# can be bent to form an integer sided right angle triangle
# in exactly one way, but there are many more examples.
# 
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# 
# In contrast, some lengths of wire, like 20 cm,
# cannot be bent to form an integer sided right angle triangle,
# and other lengths allow more than one solution to be found;
# for example, using 120 cm it is possible to form exactly three
# different integer sided right angle triangles.
# 
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# 
# Given that L is the length of the wire, for how many
# values of L <= 1,500,000 can exactly one integer sided
# right angle triangle be formed?

import math, numbers


def isRightTriangle(a,b,c):
	return a ** 2 + b ** 2 == c ** 2

def generateTriples(n):
	triples = {}
	for a in range(1, n):
		for b in range(a, n):
			c = math.floor(math.sqrt(a ** 2 + b ** 2))
			if isRightTriangle(a,b,c):
				if a in triples.keys():
					del(triples[a])
					a += 1
				else:
					triples[a] = (a,b,c)
	return triples

T = generateTriples(1000001)
print len(T)
print T[-1]