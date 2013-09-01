# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
# 
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# 
# By expanding this for the first four iterations, we get:
# 
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# 
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.
# 
# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

def denominators():
	denoms = [2, 5, 12]
	first = denoms.index(5)
	second = denoms.index(12)
	while len(denoms) < 1000:
		d = denoms[second] * 2 + denoms[first]
		denoms.append(d)
		first += 1
		second += 1
	return denoms

def numerators():
	numers = [3, 7, 17]
	first = numers.index(7)
	second = numers.index(17)
	while len(numers) < 1000:
		d = numers[second] * 2 + numers[first]
		numers.append(d)
		first += 1
		second += 1
	return numers

d = denominators()
n = numerators()

count = 0
for i in xrange(0, 1000):
	if len(str(n[i])) > len(str(d[i])):
		count += 1

print count
