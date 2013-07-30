#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

def sum_of_digits(number):
	numberWord = str(number)
	digits = []
	for letter in numberWord:
		digit = int(letter)
		digits.append(digit)
	return sum(digits)

print sum_of_digits(32768)
print "Expected: 26"

bigNumber = 2 ** 1000
print sum_of_digits(bigNumber)