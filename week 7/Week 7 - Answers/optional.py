def readfile(p_filename):
    rfile = open(p_filename, "r")
    lines = rfile.readlines()
    rfile.close()
    return lines

def writefile(p_string, p_filename):
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
    global datalist
    mystring = ""
    datalist = sorted(p_data.items(), key = lambda d:d[0])
    for term in datalist:
        term = [term[0],sorted(term[1])]
        mystring = mystring + "{:<25}{:<5}\n".format(term[0], term[1][0])
        for i in range(1,len(term[1])):
            mystring = mystring + "{:<25}{:<5}\n".format(" ",term[1][i])
        mystring += "\n"
    return mystring

def data_input():
    newdata = {}
    while True:
        state = input("User input state name: ")
        codestring = input("User input a series of area codes: ")
        if codestring == "" and state == "":
            return newdata
        else:
            codes = codestring.split()
            flag = True
            for code in codes:
                if not (len(code) == 3 and code.isdigit()):
                    print("Invalid area codes")
                    flag = False
            if flag:
                newdata[state] = codes

def data_append(p_newdata, p_data):
    for i in p_newdata:
        p_data[i] = list(set(p_data.get(i, list()) + p_newdata[i]))
    mystring = data_handle(p_data)
    return mystring

def main():
    lines = readfile("AreaCodes.txt")
    data = dict_create(lines)
    newdata = data_input()
    outputstring = data_append(newdata, data)
    writefile(outputstring, "AreaCodes_updated.txt")
    return None

main()
