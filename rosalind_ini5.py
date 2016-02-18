def main(input):
    lines = input.split("\n")
    size = len(lines) + 1		 +    results = [lines[i] for i in range(len(lines)) if i % 2]       
        return '\n'.join(lines[1:size:2]).strip()
