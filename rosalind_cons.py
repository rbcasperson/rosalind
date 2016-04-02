def main(data):
    from collections import Counter

    lines = [text.replace("\n", "") for text in data.split(">")]
    columns = zip(*[text[13:] for text in lines if text != lines[0]])
    consensus = "".join([Counter(column).most_common(1)[0][0] for column in columns])
    data = {'A': '', 'C': '', 'G': '', 'T': ''}

    for i, column in enumerate(columns):

        if i != 0:
            data['A'] += ' '
            data['C'] += ' '
            data['G'] += ' '
            data['T'] += ' '

        data['A'] += str(Counter(column)['A'])
        data['C'] += str(Counter(column)['C'])
        data['G'] += str(Counter(column)['G'])
        data['T'] += str(Counter(column)['T'])

    return '%s\nA: %s\nC: %s\nG: %s\nT: %s' % (consensus, data['A'], data['C'], data['G'], data['T'])
