n = int(input("Enter the count of list:"))
lis =[]
for i in range(n):
    lis.append(eval(input("Enter a number:")))
print("the original list is ", lis)

x = eval(input("Enter a number you want to remove:"))

# method 1
lis1 = []
for j in lis:
    if j!= x:
        lis1.append(j)
print(lis1)

# method 2
lis2 = [ e for e in lis if e != x]
print(lis2)

# method 3
lis.remove(x)
print(lis)