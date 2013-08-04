# The nth term of the sequence of triangle numbers is given by,
# tn = .5 * n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values
# we form a word value. For example, the word value
# for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
# a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

alphabet = {'A':1,
			'B':2,
			'C':3,
			'D':4,
			'E':5,
			'F':6,
			'G':7,
			'H':8,
			'I':9,
			'J':10,
			'K':11,
			'L':12,
			'M':13,
			'N':14,
			'O':15,
			'P':16,
			'Q':17,
			'R':18,
			'S':19,
			'T':20,
			'U':21,
			'V':22,
			'W':23,
			'X':24,
			'Y':25,
			'Z':26,}

def scoreWord(word):
	score = 0
	for letter in word:
		score += alphabet[letter]
	return score

def getTriangleNumbers():
	return[int(.5 * n * (n+1)) for n in range(1, 101)]


wordList = []
f = open('0042euler_words.txt', 'r')

for line in f:
	tempList = line.split(',')
	for w in tempList:
		wordList.append(w.strip('"'))
f.close()

t = getTriangleNumbers()

triangleWords = []
for word in wordList:
	if scoreWord(word) in t:
		triangleWords.append(word)

print triangleWords
print len(triangleWords)
