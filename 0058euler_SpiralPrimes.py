# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
# 
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# 
# It is interesting to note that the odd squares lie along the
# bottom right diagonal, but what is more interesting is that
# 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 is about 62%.
# 
# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square
# spiral for which the ratio of primes along both diagonals
# first falls below 10%?

# Don't create spiral. Generate the diagonal numbers instead.

from euler import is_prime

def findN():
	found = False
	n = 5
	RATIO = .1
	primesOnDiagonals = 5
	diagNums = 9.0
	while not found:
		n += 2
		diagNums += 4
		a = (n * n) - (3 * n) + 3
		b = (n * n) - (2 * n) + 2
		c = (n * n) - n + 1
		cornerNums = [a,b,c]
		for num in cornerNums:
			if is_prime(num):
				primesOnDiagonals += 1
		r = primesOnDiagonals / diagNums
		print n, r
		if r < RATIO:
			print n
			found = True

findN()
