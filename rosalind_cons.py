def main(data):
    from collections import Counter

    lines = [text.replace("\n", "") for text in data.split(">")]
    columns = zip(*[text[13:] for text in lines if text != lines[0]])
    consensus = "".join([Counter(column).most_common(1)[0][0] for column in columns])
    data = {'A': '', 'C': '', 'G': '', 'T': ''}

    for column in columns:
        data['A'] += ' ' + str(Counter(column)['A'])
        data['C'] += ' ' + str(Counter(column)['C'])
        data['G'] += ' ' + str(Counter(column)['G'])
        data['T'] += ' ' + str(Counter(column)['T'])

    return "{0}\nA:{1['A']}\nC:{1['C']}\nG:{1['G']}\nT:{1['T']}".format(consensus, data)
