def triangle_number(t):
	return t*(t+1)/2

def triangle_number_factors(n):  
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def find_500_divisors():
	n = 7
	while len(triangle_number_factors(triangle_number(n))) <= 500:
		n += 1
	return n

print triangle_number_factors(28)
print "Expected: 1, 2, 4, 7, 14, 28"

print len(triangle_number_factors(28))
print "Expected: 6"

print triangle_number(find_500_divisors())