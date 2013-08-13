# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds
# to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand
# that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the
# sum of the most consecutive primes?

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

def getPrimeSum():
	global primes
	length = 551
	for runs in range(1, 551):
		for i in range(0, runs):
			s = sum(primes[i:length-runs+i])
			if s in primes:
				return "Prime Number " + str(s), "Run " + str(runs), "i " + str(i)

print getPrimeSum()

