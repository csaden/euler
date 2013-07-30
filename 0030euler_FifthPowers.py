# Suprisingly there are only three numbers that can be written as the sum of fourth
# powers of their digits:

# 1634
# 8208
# 9474

def sumFifthPowerOfDigits(n):
	number = str(n)
	return sum([toFifth(digit) for digit in number])

def toFifth(n):
	return int(n) ** 5

fifthPowerDigits = []

number = 1
while number < 10000000:
	if sumFifthPowerOfDigits(number) == number:
		fifthPowerDigits.append(number)
	number += 1

print fifthPowerDigits
print len(fifthPowerDigits)
print sum(fifthPowerDigits)

