# An irrational decimal fraction is created by concatenating the positive
# integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part,
# find the value of the following expression.
# 
# d1 X d10 X d100 X d1000 X d10000 X d100000 X d1000000

def createDecimal(limit):
	start = 1
	decimal = "1"
	while len(decimal) <= limit - 1:
		start += 1
		decimal += str(start)
	return decimal

def champernowneConstant(d):
	decimalDigits = [d[10*i-1] for i in [1, 10, 100, 1000, 10000, 100000]]
	product = 1
	for digit in decimalDigits:
		digit = int(digit)
		product *= digit
	return product

d = createDecimal(1000000)

print champernowneConstant(d)