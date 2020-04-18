def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    n_str = input("n: ")
    try:
        n = int(n_str)
        assert n >= 0
        print(fibonacci(n))
    except:
        break



def fibo_iter(n):
    if len(fi) > n:  # have computed
        return fi[n]
    for i in range(len(fi), n+1):
        fi.append(fi[-1] + fi[-2])
    return fi[-1]


fi = [1, 1]  # use a list to remeber what have
print(fibo_iter(10))
print(fibo_iter(3))  # have computed


