# The decimal number, 585 = 1001001001  base 2 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindromeBase2(n):
	n = str(bin(n))
	forward = n[2:]
	backward = n[:1:-1]
	if forward[0] == '0' or backward[0] == '0':
		return False
	elif forward is None:
		return False
	elif forward != backward:
		return False
	else:
		return True

def isPalindromeBase10(n):
	n = str(n)
	if n[0] == '0' or n[len(n)-1] == '0':
		return False
	elif n is None:
		return False
	elif n != n[::-1]:
		return False
	else:
		return True

print sum([i for i in xrange(1, 1000000) if isPalindromeBase2(i) and isPalindromeBase10(i)])

