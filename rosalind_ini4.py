def main(input):
    a, b = input.split()
    a = int(a)
    b = int(b)
    
    sum = 0
	
    if a % 2 == 0:
        a += 1
    else:
        pass
	
    while a <= b:
        sum += a
        a += 2
		
    return sum