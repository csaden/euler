# Problem 20

# Find the sum of the digits in the number 100 factorial


def factorial(n):
	if n == 2:
		return 2
	else:
		return factorial(n-1) * n

oneHundredFactorial = factorial(100)
print oneHundredFactorial

stringFactorial = str(oneHundredFactorial)

print sum([int(x) for x in stringFactorial])