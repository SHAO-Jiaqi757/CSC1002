# def function_generator(parameters):
#   def new_function(...):
#       ...
#
#       return ...
#   return new_function


def polynomial_generator(*ws):
    def f(x):
        t = 0
        for degree, w in enumerate(ws):
            t += w * x ** degree
        return t

    print("We generate a function with weights {}".format(ws))
    return f


f = polynomial_generator(1,2)  # f = 1 + 2x
print(f(2))