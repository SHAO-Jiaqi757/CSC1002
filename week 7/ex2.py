all_lis = []
with open("AreaCodes.txt") as f:
    lines = f.readlines()
    for line in lines:
        line_lis = line.strip("\n").split("-")
        all_lis.append(line_lis)
match_dic = {}
for i in all_lis:
    match_dic[i[1]] = match_dic.get(i[1], i[0]) + " " + i[0]

with open("areacodes_file.txt", "w") as f1:
    for key, value in sorted(match_dic.items()):  
        value_all = value.split(" ")  
        f1.write("{:<20}{:<5}\n".format(key,value[0]))
        for i in sorted(value_all[1:]):
            f1.write("{:<20}{:<5}\n".format(" ",i))




