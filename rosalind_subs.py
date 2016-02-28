def main(data):
    s, t = data.strip().split("\n")
    return " ".join([str(i + 1) for i, v in enumerate(s) if s[i:(i + len(t))] == t])
