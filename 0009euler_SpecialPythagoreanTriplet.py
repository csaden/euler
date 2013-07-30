def find_ABC():
	notFound = True
	m = 2
	while notFound:
		for n in range(1, m):
			a = 2 * m * n
			b = (m * m) - (n * n)
			c = (m * m) + (n * n)
			n += 1
			if (a + b + c == 1000):
				notFound = False
				print a, b, c
				print a*b*c
			if n == m:
				m += 1
				n = 1

find_ABC()