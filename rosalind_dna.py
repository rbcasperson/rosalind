def main(input):
    from collections import Counter
    results = Counter(input)
    return " ".join(map(str, [results["A"], results["C"], results["G"], results["T"]]))
