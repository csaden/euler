
LETTER_TO_NUMBER = {
	"A":1,
	"B":2,
	"C":3,
	"D":4,
	"E":5,
	"F":6,
	"G":7,
	"H":8,
	"I":9,
	"J":10,
	"K":11,
	"L":12,
	"M":13,
	"N":14,
	"O":15,
	"P":16,
	"Q":17,
	"R":18,
	"S":19,
	"T":20,
	"U":21,
	"V":22,
	"W":23,
	"X":24,
	"Y":25,
	"Z":26
}

f = open('0022euler_names.txt', 'r')
allNames = f.read().replace('"','')
allNames = allNames.split(",")
allNames.sort()
print ""
print allNames[0]
i = 1
total = 0

for name in allNames:
	values = [LETTER_TO_NUMBER[letter] for letter in name]
	total += (i * sum(values))
	i += 1

print total