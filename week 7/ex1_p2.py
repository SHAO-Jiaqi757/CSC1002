def read_file(p_filename):
    with open(p_filename) as f:
        lines = f.readlines()
    return lines


def word_count(p_string_list):
    word_count = {}
    for line in p_string_list:
        words = line.split()
        for word in words:
            word = word.strip()
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def write_file(p_string, p_filename):
    with open(p_filename, "w") as f:
        f.write(p_string)



def main():
    lines = read_file("output.txt")
    
    word_dic = word_count(lines)
    
    file = open("word_cout_v2.txt", "w")
    for key, value in word_dic.items():
        file.write("{:<20}{:<5} \n".format(key, value))
    file.close()


if __name__ == "__main__":
    main()

