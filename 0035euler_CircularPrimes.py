
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from itertools import permutations, combinations

def isCircularPrime(n):
	for p in n:
		if not isPrime(p):
			return False
	return True

def circularPermutations(n):
	number = str(n)
	perms = []
	for i in range(0, len(number)):
		perms.append(int(number))
		number = number[1:] + number[0]
	return perms

print circularPermutations(123)
print circularPermutations(4567)

def isPrime(n):
	global primes
	if n in primes:
		return True
	else:
		return False

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

primes = sundaram3(1000000)
circularPrimes = [2]
print len(primes)

for p in primes:
	p = str(p)
	if ('2' in p or '4' in p or '6' in p or '8' in p or '0' in p):
		continue
	if isCircularPrime(circularPermutations(p)):
		circularPrimes.append(int(p))

print circularPrimes
print len(circularPrimes)
