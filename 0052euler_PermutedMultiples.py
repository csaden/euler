# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x,
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def hasSameDigits(n):
	numStrings = [str(n), str(2*n), str(3*n), str(4*n), str(5*n), str(6*n)]
	lengths = [len(num) for num in numStrings]
	if len(lengths) != lengths.count(lengths[0]):
		return False
	digits = set([digit for digit in numStrings[0]])
	for i in range(1, len(numStrings)):
		otherDigits = set([digit for digit in numStrings[i]])
		if digits != otherDigits:
			return False
	return True

answer = 1

while not hasSameDigits(answer):
	answer += 1

print answer