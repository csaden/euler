# The cube, 41063625 (345**3), can be permuted to produce two other cubes:
# 	
#	 56623104 (384**3) and 66430125 (405**3).
# 
# In fact, 41063625 is the smallest cube which has exactly three
# permutations of its digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations
# of its digits are cube.

from itertools import permutations

def getCubes():
	return [n**3 for n in range(1, 10000)]

def getPermutations(n):
	global cubes
	n = str(n)
	permutes = [int("".join(p)) for p in permutations(n)]
	return set([p for p in permutes if p in cubes])

cubes = getCubes()

for x in cubes:
	print x
	if len(getPermutations(x)) != 5:
		continue
	else:
		print "THE ANSWER IS BELOW"
		print x
		break
