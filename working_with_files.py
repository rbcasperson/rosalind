file = open('rosalind_ini5.txt', 'r')
result = open('result.txt', 'w')
lines = file.readlines()

for i in range(0, len(lines)):
	if i % 2 == 1:
		result.write(lines[i])
	else:
		pass

file.close()
result.close()
