# The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

primes = sundaram3(5000000)

def isPrimeLeft(n):
	n = str(n)
	for i in range(0, len(n)):
		num = int(n[i:])
		if isNotPrime(num):
			return False
	return True

def isPrimeRight(n):
	n = str(n)
	reverse = n[::-1]
	for j in range(0, len(reverse)):
		num = int(n[0:len(reverse)-j])
		if isNotPrime(num):
			return False
	return True

def isNotPrime(n):
	global primes
	if n not in primes:
		return True
	else:
		return False

def containsEven(n):
	n = str(n)
	if "2" in n or "4" in n or "6" in n or "8" in n or "0" in n:
		return True
	else:
		return False

truncatablePrimes = []
 
sprimes = primes[4:]
for p in sprimes:
 	if containsEven(p):
 		continue
 	if isPrimeLeft(p) and isPrimeRight(p):
 		truncatablePrimes.append(p)

truncatablePrimes.append(23)
truncatablePrimes = sorted(truncatablePrimes)
print truncatablePrimes
print sum(truncatablePrimes)
print len(truncatablePrimes)

