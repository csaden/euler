# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a^b, where a, b < 100,
# what is the maximum digital sum?

def digit_sum(n):
	nString = str(n)
	return sum([int(digit) for digit in nString])

max_sum = 0
for a in range(1,101):
	for b in range(1,101):
		power = a ** b
		d = digit_sum(power)
		if d > max_sum:
			max_sum = d
			print d
