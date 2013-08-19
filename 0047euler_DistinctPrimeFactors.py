# The first two consecutive numbers to have two distinct
# prime factors are:
# 
# 14 = 2 x 7
# 15 = 3 x 5
# 
# The first three consecutive numbers to have three distinct
# prime factors are:
# 
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
# 
# Find the first four consecutive integers to have four distinct
# prime factors. What is the first of these numbers?

from euler import is_prime, factor

def prime_factors(factorList):
	return len(factorList) == 4 

notFound = True
n = 1
while notFound:
	if prime_factors(factor(n)) and prime_factors(factor(n+1)) and prime_factors(factor(n+2)) and prime_factors(factor(n+3)):
		print n
		break
	n += 1
