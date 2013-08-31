# In the 5 by 5 matrix below, the minimal path sum from the
# top left to the bottom right, by only moving to the right and down,
# is indicated in bold red and is equal to 2427.
# 
# 
# 	131	673	234	103	18
# 	201	96	342	965	150
# 	630	803	746	422	111
# 	537	699	497	121	956
# 	805	732	524	37	331
# 
# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),
# a 31K text file containing a 80 by 80 matrix, from the top left to the
# bottom right by only moving right and down.

matrix = []

with open("0081euler_matrix.txt") as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]
	for line in lines:
		entries = line.split(',')
		entries = [int(e) for e in entries]
		matrix.append(entries)

def findSum(maze):
	gridSize = len(maze)
	for i in range(gridSize - 2, -1, -1):
		maze[gridSize - 1][i] += maze[gridSize - 1][i + 1]
		maze[i][gridSize - 1] += maze[i + 1][gridSize - 1]
	for i in range(gridSize - 2, -1, -1):
		for j in range(gridSize -2, -1, -1):
			maze[i][j] += min(maze[i + 1][j], maze[i][j+  1])
	return maze[0][0]

print findSum(matrix)