# Pentagonal numbers are generated by the formula,
# Pn=n(3n-1)/2. The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
 
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 - 22 = 48, is not pentagonal.
 
# Find the pair of pentagonal numbers, Pj and Pk,
# for which their sum and difference are pentagonal
# and D = |Pk - Pj| is minimised; what is the value of D?

def getPentagonalNumbers(max_n):
	return [n*(3*n-1)/2 for n in range(1, max_n + 1)]

def isPentagonal(a, b):
	global pents
	if a + b not in pents:
		return False
	if b - a not in pents:
		return False
	return True

pents = getPentagonalNumbers(10000)

print len(pents)

def getMorePents(l):
	for i in range(0, len(l)):
	 	for j in range(i+1, len(l)):
	 		first = l[i]
	 		second = l[j]
 			if isPentagonal(first, second):
 				print first, second, second - first
 	return "DONE"
getMorePents(pents)