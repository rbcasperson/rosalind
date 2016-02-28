def main(data):
    from itertools import combinations

    k, m, n = map(int, data.split())
    people = ("k" * k) + ("m" * m) + ("n" * n)
    options = list(combinations(people, 2))
    weights = {
        ('k', 'k'): 1,
        ('k', 'm'): 1,
        ('k', 'n'): 1,
        ('m', 'm'): 0.75,
        ('m', 'n'): 0.5,
        ('n', 'n'): 0
    }

    return sum(weights[o] for o in options) / float(len(options))
