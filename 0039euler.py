# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120:

# (20, 48, 52), (24, 45, 51), (30, 40, 50)

# for p < = 1000, what value of p produces the most solutions of integral side lengths?

import math, numbers

def isRightTriangle(a, b, c):
	if a ** 2 + b ** 2 == c ** 2:
		return True
	else:
		return False

def generateTriples(n):
	triples = []
	for a in range(1, n):
		for b in range(1, n):
			c = math.floor(math.sqrt(a ** 2 + b ** 2))
			if a ** 2 + b ** 2 == c ** 2:
				triples.append([a, b, c])
	return triples

triples = generateTriples(1001)
max_solutions = [0, 0]

for perimeter in range(0, 1001):
	solutions = 0
	for triple in triples:
		if sum(triple) == perimeter:
			solutions += 1
		if solutions > max_solutions[1]:
			max_solutions[0] = perimeter
			max_solutions[1] = solutions
			print max_solutions

