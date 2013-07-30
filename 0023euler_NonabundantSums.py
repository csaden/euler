from itertools import permutations

def properSumOfDivisors(n):
     toSum = set(x for tup in ([i, n//i] 
        for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
     toSum.remove(n)
     return sum(toSum)

def isPerfectNumber(n):
	if n == properSumOfDivisors(n):
		return True
	else:
		return False

def isdeficient(n):
	if n > properSumOfDivisors(n):
		return True
	else:
		return False

def isabundant(n):
	if n < properSumOfDivisors(n):
		return True
	else:
		return False

total = 0
abundants = []

for n in range(12, 28124):
	if isabundant(n):
		abundants.append(n)

pairSumOfAbundants = set([])


for one in abundants:
	for two in abundants:
		pairSumOfAbundants.add(one + two)

noAbundantSumPair = 0

for n in range(1, 28124):
	if n not in pairSumOfAbundants:
		noAbundantSumPair += n

print noAbundantSumPair
