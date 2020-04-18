a = [
    [100, 1, 2],
    [3, 4, 8],
    [9]
]


# row represents for each item in list_a 
sorted(a, key = lambda row: sum(row),reversed = True)