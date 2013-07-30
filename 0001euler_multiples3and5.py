results = []
for n in range(0, 1000):
	if (n % 3 == 0 or n % 5 == 0):
		results.append(n)
sum_ints = 0
for x in results:
	sum_ints+= x
print sum_ints