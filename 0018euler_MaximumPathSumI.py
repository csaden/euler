def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2

def maxChildParentPair(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)
	return a + max(b, c)

def smallerTriangle(index, rows):
	children = rows - 1
	parents = rows - 2
	left_child = 0
	right_child = 1
	new_parents = []
	for parent in index[parents]:
		new_parent = maxChildParentPair(parent, index[children][left_child], index[children][right_child])
		new_parents.append(new_parent)
		left_child += 1
		right_child += 1
	index[parents] = new_parents 
	index.remove(index[children])
	print index, len(index)
	return index, len(index)

def findMaximalPath(index, rows):
	current_index = index
	current_row = rows
	while current_row > 2:
		new_index, new_row = smallerTriangle(current_index, current_row)
		current_index, current_row = new_index, new_row
	return maxChildParentPair(current_index[0][0], current_index[1][0], current_index[1][1])

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = triangle.split("\n")

index_numbers = []
for row in triangle:
	numbers = row.split(" ")
	index_numbers.append(numbers)

print findMaximalPath(index_numbers, 15)