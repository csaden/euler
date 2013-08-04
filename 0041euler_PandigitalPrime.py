# We shall say that an n-digit number is pandigital if it makes
# use of all the digits 1 to n exactly once.
# 
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations

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

primes = sundaram3(10000000)

def makePandigitals():
	a = [''.join(x) for x in permutations('1234') if int(x[len(x)-1]) % 2 != 0]
	b = [''.join(x) for x in permutations('1234567') if int(x[len(x)-1]) % 2 != 0]
	pandigitals = a+b
	for p in pandigitals:
		last = int(p[len(p)-1])
		if last % 2 == 0:
			pandigitals.remove(p)
	return reversed(sorted([int(x) for x in pandigitals]))

def isPrime(n):
	global primes
	if n in primes:
		return True
	else:
		return False

for p in makePandigitals():
	if isPrime(p):
		print p
		break