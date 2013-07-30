def factorial(n):
	if n == 2:
		return 2
	else:
		return n * factorial(n-1) 

def gridRoutes(n):
	return factorial(2 * n) / (factorial(n) ** 2)

print factorial(4)
print "Expected: 24"
print factorial(2)
print "Expected: 2"

print gridRoutes(2)
print "Expected: 6"

print gridRoutes(20)