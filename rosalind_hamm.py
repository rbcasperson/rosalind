def main(data):
    a, b = data.strip().split('\n')
    return sum([l[0] != l[1] for l in zip(a, b)])
