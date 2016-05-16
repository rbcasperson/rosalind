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

    return "{0}\nA:{1}\nC:{2}\nG:{3}\nT:{4}".format(consensus, data['A'], data['C'], data['G'], data['T'])
