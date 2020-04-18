# change "Java" with "Python"
with open("xid-1203733_1.txt") as f:
    contents = f.read().replace("Java", "Python")
output_file = open("output.txt", "w")
output_file.write(contents)
output_file.close()

# save changed content into a new file: output.txt
with open("output.txt") as file:
    lines = file.readlines()


# count the frequency of words' occurrence.
freq = {}
for line in lines:
    for word in line.split():
        word = word.rstrip(",.:")
        freq[word] = freq.get(word, 0) + 1
Ans = sorted(freq.items(), key = lambda x: x[1], reverse = True)

count_file = open("word_count", "w")
for word_freq in Ans:
    count_file.write("{:<20} {:<5} \n".format(word_freq[0], word_freq[1]))
count_file.close()



        