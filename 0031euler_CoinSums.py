# In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# It is possible to make L2 in the following way:
# 
# 1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
# How many different ways can L2 be made using any number of coins?

solutions = []

for a in range(0, 201):
	for b in range(0, 101):
		for c in range(0, 41):
			for d in range(0, 21):
				for e in range(0, 11):
					for f in range(0, 3):
						for g in range(0, 2):
							if (a*.01 + b*.02 + c*.05 + d*.1 + e*.5 + f*1 + g*2 == 2):
								solutions.append((a, b, c, d, e, f, g))

print len(solutions)