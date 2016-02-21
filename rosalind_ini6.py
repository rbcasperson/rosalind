def main(input):
    from collections import Counter
    results = Counter([word for word in input.split()]) 
    return '\n'.join(["%s %d" % (k, v) for k, v in results.items()])