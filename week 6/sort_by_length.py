s = ["a", 'abc', 'bc']

# print(sorted(s))  # ["a", 'abc', 'bc']


# sort by length?
def get_len(string):
    return len(string)

# print(sorted(s,key=get_len))  # ['a', 'bc', 'abc']
print(sorted(s, key = lambda string: len(string)))