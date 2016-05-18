def is_in_each(sub, dna_strings):
    for dna_string in dna_strings:
        if not sub in dna_string:
            return False
    return True

def main(data):
    lines = [text.replace("\n", "") for text in data.split(">")]
    dna_strings = [line[13:]for line in lines[1:]]
    first = dna_strings.pop(0)
    lcs = ''

    for start in range(len(first) - 1):
        sub_length = 2
        while start + sub_length <= len(first):
            test_sub = first[start:start + sub_length]
            if is_in_each(test_sub, dna_strings):
                if len(test_sub) > len(lcs):
                    lcs = test_sub
                sub_length += 1
            else:
                break

    return lcs
