# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction,
# 
# less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from fractions import gcd

def reduceFraction(a, b):
	a, b = str(a), str(b)
	try:
		if a[1] == b[0]:
			if float(a[0]) / float(b[1]) == float(a) / float(b):
				if float(a) / float(b) != 1:
					return True
		elif a[0] == b[1]:
			if float(a[1]) / float(b[0]) == float(a) / float(b):
				if float(a) / float(b) != 1:
					return True
	except ZeroDivisionError:
		return False
	else:
		return False

numerator = 1
denominator = 1

for a in range(10, 100):
	for b in range(a, 100):
		if reduceFraction(a, b):
			numerator *= a
			denominator *= b

print numerator
print denominator
print gcd(a, b)

print a / gcd(a, b)
print "--"
print b / gcd(a, b)