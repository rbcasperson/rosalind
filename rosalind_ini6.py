def main(input):
    results ={}
    for word in input.split():
        try:
            results[word] += 1
        except:
            results[word] = 1       
    return '\n'.join(["%s %d" % (k, v) for k, v in results.items()])