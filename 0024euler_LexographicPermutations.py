from itertools import permutations

p = ["".join(x) for x in permutations("0123456789", 10)]

print p[999999]