def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return n

print max(x * y
	for x in range(100, 1000)
		for y in range(100, 1000)
			if is_palindrome(x*y))

print "That's all folks"