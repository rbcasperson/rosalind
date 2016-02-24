def main(data):
    from collections import Counter
    results = Counter(data)
    return "%d %d %d %d" % (results["A"], results["C"], results["G"], results["T"])
