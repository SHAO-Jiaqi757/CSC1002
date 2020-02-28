from pprint import pprint


n = 10
matrix = [
    [
        1 if j==i else 0 
        for j in range(n)
        ] 
    for i in range(n)]
pprint(matrix)
del matrix


matrix = [ [0]*i + [1] + [0]*(n-i-1)
for i in range(n)]

pprint(matrix)
del matrix


matrix = [[0]*n for k in range(n)]
for j in range(n):
    matrix[j][j] = 1

pprint(matrix)