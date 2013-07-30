def max_prime_factor(n):
	factors = []
	factor = 2
	while n > 1:
		while n % factor == 0:
			factors.append(factor)
			n /= factor
		factor = factor + 1
	print factors
	return max(factors)

print max_prime_factor(9)
print "Expected: 3"
print max_prime_factor(13195)
print "Expected: 29"
print max_prime_factor(600851475143)