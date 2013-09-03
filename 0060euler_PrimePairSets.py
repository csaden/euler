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

from itertools import permutations, combinations
from euler import is_prime

def digitSum(number):
	total = 0
	while number > 0:
		digit = number % 10
		total += digit
	return total

print digitSum(311)
print digitSum(711)
print digitSum(7109)

def getConcatenated(primes):
	primes = [str(prime) for prime in primes]
	conCats = [int(''.join(p)) for p in permutations(primes, 2)]
	for c in conCats:
		if not is_prime(c):
			return False
	return True

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

def getCombinationsFive(primes):
	for c in combinations(primes, 5):
		print c
		if getConcatenated(c):
			return c, sum(c)

p = sundaram3(10000)
p.remove(2)
p.remove(5)
getCombinationsFive(p)