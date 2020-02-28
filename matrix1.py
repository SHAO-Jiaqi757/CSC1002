from pprint import pprint # pretty printing
n = 10
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[-1].append(1 if i==j else 0)
pprint(matrix)



