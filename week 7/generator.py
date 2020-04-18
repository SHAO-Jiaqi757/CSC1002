# generator save memory
g = (x*x for x in range(4))
for i in range(4):
    print(next(g))