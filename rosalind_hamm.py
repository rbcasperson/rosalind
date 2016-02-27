def main(data):
    a, b = data.strip().split('\n')
    return sum([1 for i in range(len(a)) if a[i] != b[i]])
