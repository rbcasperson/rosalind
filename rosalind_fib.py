def main(data):
    n, k = map(int, data.split())
    rabbits = [1, 1]
    for i in range(1, n-1):
        rabbits.append(rabbits[i]+(rabbits[i-1] * k))

    return rabbits[n-1]
