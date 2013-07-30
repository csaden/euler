# The first two consecutive numbers to have two distinct prime factors are:
 
# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct prime factors # are:
 
# 644 = 2 x 2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
 
# Find the first four consecutive integers to have four distinct prime # factors
# What is the first of these numbers?

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i]=[False]*((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3 , n, 2) if sieve[i]]

def getPrimeFactors(n):
    """ Returns all the prime factors of a positive integer """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return list(set(factors))

def hasFourFactors(n):
	if len(getPrimeFactors(n)) == 4:
		return True
	else:
		return False

def nextThreeNumbers(n):
	return True if [len(getPrimeFactors(n+1)), len(getPrimeFactors(n+2)), len(getPrimeFactors(n+3))] == [4,4,4] else False

primes = primes(9999999)

for n in range(1, 999999):
	if getPrimeFactors(n) == 4:
		if nextThreeNumbers(n):
			print n
