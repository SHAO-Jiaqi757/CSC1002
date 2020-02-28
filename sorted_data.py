n = int(input("Enter the count of list:"))
data =[]
for i in range(n):
    data.append(eval(input("Enter a number:")))
print("the original data list is ", data)


## method 1: using minimum
# sorted_data1 = []
# for j in range(n):
#     minimum = min(data)
#     sorted_data1.append(minimum)
#     data.remove(minimum)

# print("The sorted data1 is ",sorted_data1)


## method 2: sort()
print(sorted(lis))
# data.sort()
# print("The sorted data2 is ",data)


# method 3
# for k in range(len(data)):
#     for w in (k, len(data)-1):
#         if data[w] < data[k]:
#             data[k], data[w] = data[w], data[k]
# print("The sorted data3 is ", data) 