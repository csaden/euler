fibs = [1,1]
term = 2

def getNextFib(fib_list):
	global term
	l = len(fib_list)
	next_fib = fib_list[l - 1] + fib_list[l - 2]
	fib_list.append(next_fib)
	fib_list.remove(fib_list[0])
	term += 1
	return fib_list

def oneThousandDigits(fib_list):
	global term
	firstFib = str(fib_list[1])
	if len(firstFib) == 1000:
		print fib_list[1]
		print
		print term
		return True
	else:
		return False

while not oneThousandDigits(fibs):
	getNextFib(fibs)

