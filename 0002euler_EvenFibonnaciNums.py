def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

total = 0
i = 1
while fib(i) < 4000000:
	if fib(i) % 2 == 0:
		total += fib(i)
	i += 1

print total