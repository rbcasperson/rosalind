def main(input):
    lines = input.split("\n")
    result = []
    length = len(lines)
    for i in range(0, length):
        if i % 2 == 1:
            result.append(lines[i])
        else:
            pass
        
    print "-" * 10    
    for line in result:
        print line
    print "-" * 10 