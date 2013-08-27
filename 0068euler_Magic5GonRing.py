# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
# and each line adding to nine.
#
#
# Working clockwise, and starting from the group of three with the
# numerically lowest external node (4,3,2 in this example),
# each solution can be described uniquely.
# For example, the above solution can be described by
# the set: 4,3,2; 6,2,1; 5,1,3.
# 
# It is possible to complete the ring with four different totals:
# 9, 10, 11, and 12. There are eight solutions in total.
# 
# Total	Solution Set
# 9		4,2,3; 5,3,1; 6,1,2
# 9		4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6
# 
# By concatenating each group it is possible to form 9-digit strings;
# the maximum string for a 3-gon ring is 432621513.
# 
# Using the numbers 1 to 10, and depending on arrangements,
# it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?

from itertools import permutations

def fiveGon():
	solutions = []
	orderings = permutations([1,2,3,4,5,6,7,8,9,10])
	for o in orderings:
		a, b, c, d, e, f, g, h, i, j = o
		if (a + b + c == d + e + b == e + g + f == g + h + i == i + c + j):
			external_nodes = [a, d, f, h, j]
			lowest = external_nodes.index(min(external_nodes))
			a, b, c, d, e, f, g, h, i, j = str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i), str(j)
			if lowest == 0:
				solutions.append(a+b+c+j+c+i+h+i+g+f+g+e+d+e+b)
			if lowest == 1:
				solutions.append(d+e+b+a+b+c+j+c+i+h+i+g+f+g+e)
			if lowest == 2:
				solutions.append(f+g+e+d+e+b+a+b+c+j+c+i+h+i+g)
			if lowest == 3:
				solutions.append(h+i+g+f+g+e+d+e+b+a+b+c+j+c+i)
			if lowest == 4:
				solutions.append(j+c+i+h+i+g+f+g+e+d+e+b+a+b+c)
	numbers = []
	for s in solutions:
		if len(s) == 16:
			s = int(s)
			numbers.append(s)
	return max(numbers)

print fiveGon()
