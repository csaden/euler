#A unit fraction contains 1 in the numerator. The decimal representation of the 
# unit fractions with denominators 2 to 10 are given...

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# find the primes less than 1000
# look at their outputs for their reciprocals

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

def findRepeatingDecimal(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k, z / d

primes = sundaram3(1000)

repeatingdecimals = [[d, findRepeatingDecimal(1, d)] for d in primes[3:]]

max_repeat = max(repeatingdecimals[i][1][0] for i in range(len(repeatingdecimals)))

for i in range(0, len(repeatingdecimals)):
    if repeatingdecimals[i][1][0] == max_repeat:
        print repeatingdecimals[i]