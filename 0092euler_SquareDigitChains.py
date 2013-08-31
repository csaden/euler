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
leadsTo1 = set()

def squareChain(n):
	global leadsTo89, leadsTo1
	unique = True
	terms = set([n])
	while unique: 
		digits = [int(d) for d in str(n)]
		newTerm = 0
		for digit in digits:
			newTerm += digit ** 2
		print newTerm, terms
		if newTerm == 89 or newTerm in leadsTo89:
			leadsTo89 = leadsTo89 | terms
			return 89
		elif newTerm == 1 or newTerm in leadsTo1:
			leadsTo1 = leadsTo1	| terms
			return 1
		else:
			terms.add(newTerm)
			n = newTerm

chains89 = 0
for num in numbers:
	if squareChain(num) == 89:
		chains89 += 1

print chains89