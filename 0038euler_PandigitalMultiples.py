# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can
# be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1?

def isPandigital(n):
	digits = [digit for digit in n]
	digits = sorted(digits)
	if digits == ['1','2','3','4','5','6','7','8','9']:
		return True
	else:
		return False

def isOneDigit():
	solutions = []
	for n in range(1, 10):
		num = str(n * 1) + str(n * 2) + str(n * 3) + str(n * 4) + str(n * 5) 
		if len(num) != 9:
			continue
		if isPandigital(num):
			solutions.append(num)
	return None if len(solutions) == 0 else max(solutions)

def isTwoDigit():
	solutions = []
	for n in range(10, 99):
		num = str(n * 1) + str(n * 2) + str(n * 3) + str(n * 4)
		if len(num) != 9:
			continue
		if isPandigital(num):
			solutions.append(num)
	return None if len(solutions) == 0 else max(solutions)

def isThreeDigits():
	solutions = []
	for n in range(100, 1000):
		num = str(n * 1) + str(n * 2) + str(n * 3)
		if len(num) != 9:
			continue
		if isPandigital(num):
			solutions.append(num)
	return None if len(solutions) == 0 else max(solutions)

def isFourDigits():
	solutions = []
	for n in range(10, 10000):
		num = str(n * 1) + str(n * 2)
		if len(num) != 9:
			continue
		if isPandigital(num):
			solutions.append(num)
	return None if len(solutions) == 0 else max(solutions)

def isFiveDigits():
	solutions = []
	for n in range(10, 10000):
		num = str(n * 1) + str(n * 2)
		if len(num) != 9:
			continue
		if isPandigital(num):
			solutions.append(num)
	return None if len(solutions) == 0 else max(solutions)

print isOneDigit()
print isTwoDigit()
print isThreeDigits()
print isFourDigits()
print isFiveDigits()