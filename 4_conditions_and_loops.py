def sum_odds(a, b):
	sum = 0
	
	if a % 2 == 0:
		a += 1
	
	while a <= b:
		sum += a
		a += 2
		
	return sum
	
a = 4397
b = 8698

print sum_odds(a,b) #14082597
