# Method 1 ( Use recursion )
# A simple method that is a direct recursive implementation 
# mathematical recurrence relation given above.

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(9))



# Method 2 ( Use Dynamic Programming )
# We can avoid the repeated work done is the method 1 
# by storing the Fibonacci numbers calculated so far.

def fibonacci(n):
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
       return n
    else:
       if FibArray[n - 1] == 0:
           FibArray[n - 1] = fibonacci(n - 1)
       if FibArray[n - 2] == 0:
           FibArray[n - 2] = fibonacci(n - 2)
       FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]

print(fibonacci(9))



# Method 3 (Space Optimized Method)
# We can optimize the space used in method 2 by storing the previous two numbers 
# only because that is all we need to get the next Fibonacci number in series.

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))


# Method 4
# with O(Log n) arithmatic operations
MAX = 1000

# Create an array for memoization
f = [0] * MAX

# Returns n'th fuibonacci number using table f[]


def fib(n):
    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]):
        return f[n]

    if(n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applyting above formula [Note value n&1 is 1]
    # if n is odd, else 0.
    if((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]

n = 9
print(fib(n))
