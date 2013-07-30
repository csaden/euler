# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

total = 0

for number in xrange(100,300000): # No such 2 or 3 digit number exists and max value 5*(9^5)
    l = [factorials[int(digit)] for digit in str(number)]
    if sum(l) == number:
        total += number
        print number
print 'Total of these numbers = ' + str(total)
