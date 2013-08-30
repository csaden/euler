# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
# number, 134217728=89, is a ninth power.
# 
# How many n-digit positive integers exist which are also an nth power?

def nthPowers():
	nthPowers = 0
	nP = ((x ** y, x, y) for x in range(1, 200) for y in range(1, 200))
	for calc in nP:
		if len(str(calc[0])) == calc[2]:
			print calc
			nthPowers += 1
	return nthPowers

print nthPowers()