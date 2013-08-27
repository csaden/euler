# The first known prime found to exceed one million digits was discovered in 1999,
# and is a Mersenne prime of the form 2^6972593-1;
# it contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
# of the form 2p-1, have been found which contain more digits.
# 
# However, in 2004 there was found a massive non-Mersenne prime
# which contains 2,357,207 digits: 28,433*2^7830457+1.
# 
# Find the last ten digits of this prime number.

def power_of_two():
	power = 1
	for n in range(1, 7830458):
		power *= 2
		power = str(power)
		if len(power) > 10:
			power = power[:-11:-1]
			power = power[::-1]
			power = int(power)
	power = int(power)
	return power

p = power_of_two()
nMprime = (p * 28433) + 1
print nMprime

