def main(data):
    a, b = data.split('\n')
    hamm_dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hamm_dist += 1
        else:
            pass
    return hamm_dist
