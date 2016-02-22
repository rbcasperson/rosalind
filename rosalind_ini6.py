def main(input):
    from collections import Counter
    results = Counter(input.split())
    return '\n'.join(["%s %d" % (k, v) for k, v in results.items()])
