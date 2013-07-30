def isCircularPrime(n):
	global primes
	for p in permutationsOfDigits(n):
		if p not in primes: return False
	return True

def permutationsOfDigits(n): 197 179 791 719 971 917
	permutations = []
	number = str(n)
	l = len(number) l = 3
	digits = [digit for digit in number]
	
	return permutations

def isPrime(n):
	global primes
	if n in primes: return True

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

primes = sundaram3[]