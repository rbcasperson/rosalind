def main(input):
    from collections import Counter
    results = Counter(input)
    return "%d %d %d %d" % (results["A"], results["C"], results["G"], results["T"])
