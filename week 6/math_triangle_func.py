from math import sin, cos, tan

def f1(x):
    return x**2

def f2(x):
    return x * 2

f_str = input("choose 'sin','cos','tan','f1' or 'f2'?:")

# if f == "sin":
#     f = sin  # build_in function

# elif f == "cos":
#     f = cos  # bulid_in function

# elif f == "tan":
#     f = tan  # build_in function

# elif f == "f1":
#     f = f1
# elif f == "f2":
#     f = f2


mapping = {
    "sin":sin,
    "cos":cos,
    "tan":tan,
    "f1":f1,
    "f2":f2
}

if f_str in mapping:
    f = mapping[f_str]

x = float(input("x: "))

print(f(x))