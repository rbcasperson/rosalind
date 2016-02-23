def main(data):
    from collections import Counter
    results = Counter(data)
    return " ".join(map(str, [results["A"], results["C"], results["G"], results["T"]]))
