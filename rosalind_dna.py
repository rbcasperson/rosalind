def main(input):
    from collections import Counter
    results = dict(Counter(sorted(list(input))))
    return " ".join(map(str, [results["A"], results["C"], results["G"], results["T"]]))