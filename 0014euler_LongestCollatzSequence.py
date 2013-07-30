def Collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def Collatzing(start):
	chain = []
	number = start
	while number != 1:
		chain.append(number)
		number = Collatz(number)
	chain.append(1)
	return chain, len(chain)

print Collatzing(13)
print "Expected: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]"

longest_chain = 1

for n in range(2, 1000001):
	is_longer = Collatzing(n)
	if is_longer[1] > longest_chain:
		longest_chain = is_longer[1]
		longest = is_longer
print longest