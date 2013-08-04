# It was proposed by Christian Goldbach that every odd composite
# number can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2
# 
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?

def getSquares(max_n):
	return [n*n for n in range(1, max_n + 1)]

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

n = 10000
sQ = getSquares(n)
pR = sundaram3(n)

print sQ
print pR

def isPrime(n):
	global pR
	if n in pR:
		return True
	return False

def isPrimePlusDoubleSquare(n, primes, squares):
	for x in primes:
		if x < n:
			for y in squares:
				if y < n:
					if x + (2 * y) == n:
						print x, y, n
						return True
	return False


found = False
num = 1
while not found:
	num += 2
	if isPrime(num):
		continue
	if isPrimePlusDoubleSquare(num, pR, sQ):
		continue
	print num
	found = True

print
print "-"*10 + "Done" + "-"*10

