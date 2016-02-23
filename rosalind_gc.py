def main(data):
    lines = [text.replace("\n", "") for text in data.split(">")]
    pairs = {text[:13]: text[13:]for text in lines if text != lines[0]}
    cg_percents = {k: ((pairs[k].count("C") + pairs[k].count("G")) / float(len(pairs[k]))) * 100 for k in pairs}
    highest = max(cg_percents.values())
    answer = ["%s\n%f" % (k, v) for k, v in cg_percents.items() if v == highest]
    return answer[0]
