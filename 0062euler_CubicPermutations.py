# The cube, 41063625 (345**3), can be permuted to produce two other cubes:
# 	
#	 56623104 (384**3) and 66430125 (405**3).
# 
# In fact, 41063625 is the smallest cube which has exactly three
# permutations of its digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations
# of its digits are cube.

from itertools import permutations, chain

cubes = {}
results = {}

def getLargest(n):
	strN = str(n)
	digits = [d for d in strN]
	digits = "".join(digit for digit in chain(sorted(digits, reverse=True)))
	return int(digits)

def generateCubes():
 	n = 1
 	while 5 not in results.values():
 		cube = n * n * n
 		print n, cube
 		maxPerm = getLargest(cube)
 		if maxPerm not in results.keys():
 			results[maxPerm] = 1
 			cubes[maxPerm] = [n]
 			print results[maxPerm]
 			n += 1
 		else:
 			results[maxPerm] += 1
 			cubes[maxPerm].append(n)
			print results[maxPerm]
 			n += 1
 	for k, v in results.iteritems():
 		if v == 5:
 			return k

iD = generateCubes()
print iD
print cubes[iD]
smallN = cubes[iD][0]
answer = smallN ** 3
print answer