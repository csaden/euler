# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order
# the result will always be prime.
# 
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum
# for a set of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any
# two primes concatenate to produce another prime.

from itertools import combinations
from euler import is_prime

def getConcatenated(primes):
	forward = [str(primes[i]) for i in range(0, len(primes))]
	for i in range(0, len(primes)):
		for j in range(i+1, len(primes)):
			twoNums = int(forward[i] + forward[j])
			if not is_prime(twoNums):
				return False
	for i in range(len(primes)-1, -1, -1):
		for j in range(i-1, -1, -1):
			backNums = int(forward[i]+forward[j])
			if not is_prime(backNums):
				return False
	return True

print getConcatenated((3,7,109,673))

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def getCombinationsFive(primeList):
	for c in combinations(primeList, 5):
		print c
		if getConcatenated(c):
			return c, sum(c)

p = sundaram3(1000)
p.remove(2)
p.remove(5)
getCombinationsFive(p)