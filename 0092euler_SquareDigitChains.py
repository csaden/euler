# A number chain is created by continuously adding the square of
# the digits in a number to form a new number until it has been seen before.
# 
# For example,
# 
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# 
# Therefore any chain that arrives at 1 or 89 will become
# stuck in an endless loop. What is most amazing is that
# EVERY starting number will eventually arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

leadsTo89 = set()

def squareChain(n):
	global leadsTo89
	unique = True
	terms = set([n])
	while unique: 
		digits = [int(d) for d in str(n)]
		newTerm = 0
		for digit in digits:
			newTerm += digit ** 2
		if newTerm == 89:
			leadsTo89 = leadsTo89 | terms
			return 89
		elif newTerm in leadsTo89:
			leadsTo89 = leadsTo89 | terms
			return 89
		elif newTerm in terms:
			return newTerm
		else:
			terms.add(newTerm)
			n = newTerm

chains89 = 0
for x in range(1,10000000):
	if squareChain(x) == 89:
		chains89 += 1

print chains89