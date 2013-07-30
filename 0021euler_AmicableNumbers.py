#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def properSumOfDivisors(n):
     toSum = set(x for tup in ([i, n//i] 
        for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
     toSum.remove(n)
     return sum(toSum)

def amicablePair(a, b):
	if a != b and properSumOfDivisors(a) == b and properSumOfDivisors(b) == a:
		return True
	else:
		return False

def createAmicableDict(n):
	amicable_Numbers = {}
	for i in range(1, n+1):
		amicable_Numbers[i] = properSumOfDivisors(i)
	print amicable_Numbers
	return amicable_Numbers

def findAmicablePairs(amicableDict):
	total = 0
	copy = amicableDict.copy()
	for k, v in amicableDict.iteritems():
		if k == v or v >= 10001:
			continue
		if copy.get(k) == v and copy.get(v) == k:
			print (v, k)
			total = total + k + v
			print total
	return total / 2

print findAmicablePairs(createAmicableDict(10001))
