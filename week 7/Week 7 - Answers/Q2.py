def read_file(p_filename):
    rfile = open(p_filename, "r")
    lines = rfile.readlines()
    rfile.close()
    return lines

def write_file(p_string, p_filename):
    wfile = open(p_filename, "w")
    wfile.write(p_string)
    wfile.close()
    return None

def dict_create(p_lines):
    global data
    data = {}
    for line in p_lines:
        terms = line[:-1].split("-")
        data[terms[1]] = list(set(data.get(terms[1], list()) + [terms[0]]))
    return data

def data_handle(p_data):
    global data_list
    my_string = ""
    data_list = sorted(p_data.items(), key = lambda d:d[0])
    for term in data_list:
        term = [term[0],sorted(term[1])]
        my_string = my_string + "{:<25}{:<5}\n".format(term[0], term[1][0])
        for i in range(1,len(term[1])):
            my_string = my_string + "{:<25}{:<5}\n".format(" ",term[1][i])
        my_string += "\n"
    return my_string


def main():
    lines = read_file("AreaCodes.txt")
    data = dict_create(lines)
    output_string = data_handle(data)
    write_file(output_string, "AreaCodes_GOOD.txt")
    return None


if __name__ == '__main__':
    main()
