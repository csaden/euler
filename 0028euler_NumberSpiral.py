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

def createSquare(n, number, spiral):
	for n in range(n,-1,-1):
		spiral[n-n][n] = number
		number -= 1
	for n in range(1,n):


	


def createSpiral(n):
	number = n * n
	row = [0 for n in range (0, n)]
	spiral = [row for n in range(0, n+1)]
	for

	for row in spiral:
		print row


createSpiral(5)