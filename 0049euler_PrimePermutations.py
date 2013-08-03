# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# 		(i) each of the three terms are prime, and
# 		(ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

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

primes = sundaram3(10000)

def isNotPrime(number):
	global primes
	if number in primes:
		return False
	else:
		return True

def isTripleOfPerumtations(numbers):
    firstPerm = str(numbers[0])
    stringPerms = [p for p in permutations(firstPerm)]
    intPerms = []
    for s in stringPerms:
        joinedString = ''.join(s)
        intPerms.append(int(joinedString))
    for i in range(1, len(numbers)):
        if numbers[i] not in intPerms:       
            return False
    return True

def hasConstantDifference(nums):
    triples = []
    n = len(nums)
    for i in range(0, n):
        if nums[i] < 3000:
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[j] - nums[i] == nums[k] - nums[j]:
                        triple = [nums[i], nums[j], nums[k]]
                        if isTripleOfPerumtations(triple):
                         triples.append(triple)
    return triples

fourDigitPrimes = []
for p in primes:
	if len(str(p)) == 4:
		fourDigitPrimes.append(p)

answers = hasConstantDifference(fourDigitPrimes)
print answers

solution = ''
for primeElement in answers[1]:
    z = str(primeElement)
    solution += z
print solution

