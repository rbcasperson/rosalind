def main(input):
    work_list = list(input[::-1])
    for i in range(len(work_list)):
        if work_list[i] == "A":
            work_list[i] = "T"
        elif work_list[i] == "T":
            work_list[i] = "A"
        elif work_list[i] == "C":
            work_list[i] = "G"
        elif work_list[i] == "G":
            work_list[i] = "C"
    return "".join(work_list)
