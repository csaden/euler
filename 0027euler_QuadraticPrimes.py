 
# Euler discovered the remarkable quadratic formula:
# 
# n^2 + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 
# is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
# divisible by 41.
# 
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces
# 80 primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.
# 
# Considering quadratics of the form:
# 
#     n^2 + an + b, where |a| < 1000 and |b| < 1000
# 
#     where |n| is the absolute value of n
#     e.g. |11| = 11 and |-4| = 4
# 
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

def isPrime(n):
	global primes
	if n not in primes:
		return False
	else:
		return True

def getPrimes(a, b):
	primesList = []
	if a == 1:
		limit = abs(b) - 1
	else:
		limit = abs(a) + 1
	for n in range(0, limit):
		possiblePrime = (n*n)+(a*n)+b
		if isPrime(possiblePrime):
			primesList.append(possiblePrime)
		else:
			return
	return sorted(primesList)

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

longest = 1
coefficients = sundaram3(1000)
coefficients.insert(0,1)

def getAandB():
	global longest, coefficients
	for a in coefficients:
		for b in coefficients:
	  		p = getPrimes(a,b)
	  		if p == None:
	  			continue
	  		if len(p) > longest:
	  			longest = len(p)
	  			print a, b, a*b, "Length:" + str(len(p))

def getNegativeAandB():
	global coefficients, longest
	negatives = []
	for x in coefficients:
		x *= -1
		negatives.append(x)
	for a in negatives:
		for b in coefficients:
	  		p = getPrimes(a,b)
	  		if p == None:
	  			continue
	  		else:
	  			if len(p) > longest:
	  				print a, b, a*b, "Length:" + str(len(p))
getAandB()
getNegativeAandB()
