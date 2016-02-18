def main(input):
    words = input.split()
    results ={}
    for word in words:
        try:
            results[word] += 1
        except:
            results[word] = 1
            
    for k in results:
        print "%s %d" % (k, results[k])