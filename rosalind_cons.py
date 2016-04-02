def main(data):
    from collections import Counter

    lines = [text.replace("\n", "") for text in data.split(">")]
    columns = zip(*[text[13:] for text in lines if text != lines[0]])
    consensus = "".join([Counter(column).most_common(1)[0][0] for column in columns])

    a = " ".join([str(Counter(column)['A']) for column in columns])
    c = " ".join([str(Counter(column)['C']) for column in columns])
    g = " ".join([str(Counter(column)['G']) for column in columns])
    t = " ".join([str(Counter(column)['T']) for column in columns])

    return '%s\nA: %s\nC: %s\nG: %s\nT: %s' % (consensus, a, c, g, t)
