def sum_of_squares(max_val):
	return sum([n ** 2 for n in range(0, max_val+1)])

def square_of_sums(max_val):
	return (sum([x for x in range(0, max_val+1)]) ** 2)

print sum_of_squares(10)
print "Expected: 385"
print square_of_sums(10)
print "Expected: 3025"
print abs(sum_of_squares(10)-square_of_sums(10))
print abs(sum_of_squares(100)-square_of_sums(100))