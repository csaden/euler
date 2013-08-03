# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
# is formed as follows...

# 	21	22	23	24	25
# 	20	7	8	9	10
# 	19	6	1 	2 	11
# 	18	5	4	3	12
# 	17	16	15	14	13

# It can be verified that the sum of the numbers on the diagonal is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the
# same way?

n = input("Enter the size of n for an 'n by n' spiral: ")
x = (n-1)/2
y = (n-1)/2 

def moves(n):
	global x, y
	if n % 4 == 0:
		y += 1
		return
	elif n % 4 == 1:
		x += 1
		return
	elif n % 4 == 2:
		y -= 1
		return
	else:
		x -= 1
		return

def createSpiral(num):
	global n, x, y
	largest = num * num
	spiral = [[0 for r in range (0, n)] for c in range(0, n)]
	spiral[(n-1)/2][(n-1)/2] = 1

	direction = 0
	current = 1
	occurences = 1

	while current < largest and occurences <= n-1:
		for a in range(0, 2):
			for b in range(0, occurences):
				current += 1
				moves(direction)
				spiral[x][y] = current
				print x, y
			direction+= 1
		occurences += 1
	
	direction += 1
	for c in range(0, n - 1):
		current += 1
		moves(direction)
		spiral[y][x] = current
		print x, y
	for x in spiral:
		print x
	return spiral

def sumdiagonals(spiral):
	global n
	diagDownRight = 0
	for i in range(0, n):
		for j in range(0, n):
			if i == j:
				diagDownRight += spiral[i][j]
	diagUpRight = 0
	i, j = 0, n-1
	for z in range(0, n):
		diagUpRight += spiral[j][i]
		j -= 1
		i += 1
	return diagDownRight + diagUpRight - 1

s = createSpiral(n)
print sumdiagonals(s)