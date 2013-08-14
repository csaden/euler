# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
# 
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# 
# It is interesting to note that the odd squares lie along the
# bottom right diagonal, but what is more interesting is that
# 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 is about 62%.
# 
# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square
# spiral for which the ratio of primes along both diagonals
# first falls below 10%?

# Don't create spiral. Generate the diagonal numbers instead.

# def moves(n, pos):
# 	if n % 4 == 0:
# 		pos[1] += 1
# 		return pos
# 	elif n % 4 == 1:
# 		pos[0] += 1
# 		return pos
# 	elif n % 4 == 2:
# 		pos[1] -= 1
# 		return pos
# 	else:
# 		pos[0] -= 1
# 		return pos
# 
# def createSpiral(num):
# 	pos = [(num-1)/2, (num-1)/2]
# 	largest = num * num
# 	spiral = [[0 for r in range (0, num)] for c in range(0, num)]
# 	spiral[(num-1)/2][(num-1)/2] = 1
# 
# 	direction = 0
# 	current = 1
# 	occurences = 1
# 
# 	while current < largest and occurences <= num-1:
# 		for a in range(0, 2):
# 			for b in range(0, occurences):
# 				current += 1
# 				pos = moves(direction, pos)
# 				spiral[pos[0]][pos[1]] = current 
# 			direction+= 1
# 		occurences += 1
	# 
# 	direction += 1
# 	for c in range(0, num - 1):
# 		current += 1
# 		pos = moves(direction, pos)
# 		spiral[pos[1]][pos[0]] = current
# 	return spiral

def getDiagonalNumbers(n):
	diagNums = [1]
	primeNums
	for i in range(3, n, 2):
		a = (i * i) - (3 * i) + 3
		b = (i * i) - (2 * i) + 2
		c = (i * i) - i + 1
		d = i * i
		cornerNums = [a,b,c,d]



def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

primes = sundaram3(1000000)

def isPrime(n):
	global primes
	if n in primes:
		return True
	return False

def getDiagonalPrimesRatio(spiral):
	n = len(spiral)
	diagDownRightPrimes = 0
	for i in range(0, n):
		for j in range(0, n):
			if i == j:
				if isPrime(spiral[i][j]):
					diagDownRightPrimes += 1
	diagUpRightPrimes = 0
	i, j = 0, n-1
	for z in range(0, n):
		if isPrime(spiral[j][i]):
			diagUpRightPrimes += 1
		j -= 1
		i += 1
	return (diagDownRightPrimes + diagUpRightPrimes) / (2*n - 1.0)

def findN():
	notfound = True
	n = 5
	while notfound:
		s = createSpiral(n)
		r = getDiagonalPrimesRatio(s)
		print n, r
		if r < .095:
			print "******************HERE'S THE ANSWER******************"
			print n, r
			notfound = False
		n += 2
findN()
