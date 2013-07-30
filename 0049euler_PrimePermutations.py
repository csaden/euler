# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# 		(i) each of the three terms are prime, and
# 		(ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import combinations, permutations

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

primes = sundaram3(10000)

def isPrime(number):
	global primes
	if number in primes:
		return True
	else:
		return False

def isPerumtation(numbers):
	pass

fourDigitPrimes = []

for p in primes:
	if len(str(p)) == 4:
		fourDigitPrimes.append(p)

print fourDigitPrimes

x = list(combinations(fourDigitPrimes, 3))
print x[0]
print type(x[0])
print type(x[0][0])
