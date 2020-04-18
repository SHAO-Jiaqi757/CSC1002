def read_file(p_filename):
    r_file = open(p_filename, "r")
    lines = r_file.readlines()
    r_file.close()
    return lines


def word_count(p_string_list):
    freq = {}
    my_string = ""
    for line in p_string_list:
        for word in line.split():
            freq[word] = freq.get(word,0) + 1
    freq = sorted(freq.items(), key = lambda d:d[1], reverse = True)
    for w in freq:
        my_string = my_string + "{:<20}{:<5}\n".format(w[0], w[1])
    return my_string
    

def write_file(p_string, p_filename):
    w_file = open(p_filename, "w")
    w_file.write(p_string)
    w_file.close()
    return None

def main():
    string_list = read_file("the_best_programming_language.txt")   
    word_count_string = word_count(string_list)
    write_file(word_count_string, "def_word_count.txt")


if __name__ == '__main__':
    main()

