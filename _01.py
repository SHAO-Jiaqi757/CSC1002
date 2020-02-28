import random
def swap(l, j):
    l[j],l[j+1] = l[j+1],l[j]

l = list(range(10))
random.shuffle(l)
print('before:',l)

for i in range(len(l)):
    # print('hi',i)
    for j in range(0,len(l)-1-i):
        if l[j] > l[j+1]:
            swap(l, j)
            #l[j],l[j+1] = l[j+1],l[j] 

print('after:',l) 