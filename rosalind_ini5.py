def main(input):
    lines = input.split("\n")
    results = [lines[i] for i in range(len(lines)) if i % 2]
        
    print "-" * 10    
    for line in results:
        print line 
    print "-" * 10 