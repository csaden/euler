# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once.
# For example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only 
# include it once in your sum.

def isPandigit(n):
	if ''.join(sorted([str(d) for d in str(n)])) == "123456789":
		return True
	else:
		return False

products = set([])

for n in range(1, 9999):
	for m in range(1, 99):
		product = n * m
		if isPandigit(str(n) + str(m) + str(product)):
			print n, m, product
			products.add(product)

print products
print sum(products)

