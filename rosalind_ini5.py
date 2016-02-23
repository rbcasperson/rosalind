def main(data):
    lines = data.split("\n")
    size = len(lines) + 1
    return '\n'.join(lines[1:size:2]).strip()
