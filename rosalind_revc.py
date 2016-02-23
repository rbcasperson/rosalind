def main(input):
    original_list = list(input[::-1])
    translate_list = ["T" if x == "A" else "A" if x == "T" else "G" if x == "C" else "C" for x in original_list[1:]]
    return "".join(translate_list)
