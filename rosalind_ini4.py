def main(data):
    a, b = map(int, data.split())
    return sum([i for i in range(a, b + 1) if i % 2])
