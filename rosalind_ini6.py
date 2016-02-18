def main(input):
    results ={}
    for word in input.split():
        try:
            results[word] += 1
        except:
            results[word] = 1
            
    for k, v in results.items():
        print "%s %d" % (k, v)