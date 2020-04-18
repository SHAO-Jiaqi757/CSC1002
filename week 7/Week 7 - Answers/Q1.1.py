my_file = open("the_best_programming_language.txt", "r")
lines = my_file.readlines()
my_file.close()

freq = {}
for i in range(len(lines)):
    lines[i] = lines[i].replace("Java", "Python")
    for word in lines[i].split():
        word = word.rstrip(',.:')
        freq[word] = freq.get(word,0) + 1

my_file = open("output.txt", "w")
my_file.write("".join(lines))
my_file.close()

freq = sorted(freq.items(), key = lambda d:d[1], reverse = True)
print(freq)

new_file = open("word_count.txt", "w")
for w in freq:
   new_file.write("{:<20}{:<5}\n".format(w[0], w[1]))
new_file.close()