# The number, 1406357289, is a 0 to 9 pandigital number because
# it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

def isDivisible(n):
	substrings = []
	for pos in range(1, 8):
		substrings.append(int(n[pos:pos+3]))
	divisors = [2, 3, 5, 7, 11, 13, 17]
	for index in range(0, 7):
		if substrings[index] % divisors[index] != 0:
			return False
	return True

def getNineDigitPandigitals():
	return [''.join(x) for x in permutations('0123457689') if (x[0] != '0' and x[3] in ['0', '2', '4', '6', '8'] and x[5] in ['0', '5'])]

p = getNineDigitPandigitals()
answers = [int(num) for num in p if isDivisible(num)]
print answers
print sum(answers)
