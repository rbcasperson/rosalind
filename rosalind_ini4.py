def main(input):
    a, b = map(int, input.split())

    return sum([i for i in range(a, b + 1) if i % 2])
