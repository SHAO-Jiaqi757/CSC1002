l = [1,2,3]
l2 = l.__iter__()
# print(l2.__next__())  # l[0] = 1
# print(l2.__next__())  # l[1] = 2
# print(l2.__next__())  # l[2] = 3

for i in l:
    print(i, end=" ")

for i in l2:
    print(i ,end=" ")


class Sequence:
    def __init__(self):
        self.x = 0
    def __next__(self):
        self.x += 1

        if (self.x > 14):
            raise StopIteration

        return self.x ** self.x

    def __iter__(self):
        return self



s = Sequence()
n = 0
for w  in s:
    print(w)
    n += 1
    if n >10:
        break