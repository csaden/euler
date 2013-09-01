# The square root of 2 can be written as an infinite continued fraction.
# 
# The infinite continued fraction can be written, sqrt(2) = [1;(2)],
# (2) indicates that 2 repeats ad infinitum. In a similar way, sqrt(23) = [4;(1,3,1,8)].
# 
# It turns out that the sequence of partial values of continued fractions
# for square roots provide the best rational approximations.
# Let us consider the convergents for sqrt(2).
# 
#  
# Hence the sequence of the first ten convergents for sqrt(2) are:
# 
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# 
# The first ten terms in the sequence of convergents for e are:
# 
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# 
# Find the sum of digits in the numerator of the 100th convergent of
# the continued fraction for e.

from fractions import Fraction

def getDigitSum(n):
	total, num = 0, n
	while num > 0:
		total += num % 10
		num /= 10
	return total

def getFractionTest():
	divisions = []
	seqs = ([1, 2*k, 1] for k in xrange(1, 4))
	for seq in seqs:
		divisions.extend(seq)
	denom = divisions.pop()
	value = 0
	while len(divisions) > 0:
		value = 1.0 / denom
		denom = divisions.pop() + value
	value = 1.0 / denom
	value += 2
	return Fraction(value).limit_denominator()

def solve():
    i = 11
    current = 1457
    backOneNum = 1264
    backTwoNums = 0
    multiple = 8

    while i <= 100:
	backTwoNums = backOneNum
	backOneNum = current

	if i%3 == 0:
	    current = backOneNum*multiple + backTwoNums
	    multiple += 2
 	else:
	    current = backOneNum + backTwoNums

	i += 1

    return sum(map(int, str(current)))

print solve()
