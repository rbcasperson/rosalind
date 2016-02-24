def main(data):
    from collections import Counter
    results = Counter(data.split())
    return '\n'.join(["%s %d" % (k, v) for k, v in results.items()])
