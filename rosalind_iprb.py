def main(data):
    from itertools import combinations
    from collections import Counter

    k, m, n = map(int, data.split())
    people = ("k" * k) + ("m" * m) + ("n" * n)
    options = list(combinations(people, 2))
    total = float(len(options))
    c = dict(Counter(options))
    chance_k = (c[('k', 'k')] + c[('k', 'm')] + c[('k', 'n')]) / total
    chance_mn = (c[('m', 'n')] / total) * .5
    chance_mm = (c[('m', 'm')] / total) * .75
    return chance_k + chance_mn + chance_mm
