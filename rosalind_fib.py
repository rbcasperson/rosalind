def main(input):
    n, k = map(int, input.split())
    rabbits = [1, 1] 
    for i in range(1, n-1):
        rabbits.append(rabbits[i]+(rabbits[i-1] * k))
        
    return rabbits[n-1]
        