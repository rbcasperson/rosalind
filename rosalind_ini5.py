def main(input):
    lines = input.split("\n")
    results = [lines[i] for i in range(len(lines)) if i % 2]       
    return "\n".join([line for line in results])