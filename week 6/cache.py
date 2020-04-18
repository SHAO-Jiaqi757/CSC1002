import time 

def sleepy(n):
    time.sleep(1)  # sleep for 1 second
    return n 

# @cache
# def sleepy2(n):  # same as sleepy1
#     time.sleep(1)  # sleep for 1 second
#     return n  



def cache(function):
    def wrapper(n):
        if n in knowledge:
            return knowledge[n]
        else:
            result = function(n)
            knowledge[n] = result
            return result
    knowledge = {}
    return wrapper

sleepy1 = cache(sleepy)
sleepy3 = cache(sleepy)

print(sleepy1(1))
print(sleepy1(2))
print(sleepy1(3))
print(sleepy1(1))
print(sleepy1(1))
print(sleepy1(1))


# different cache knowledge!!!
print(sleepy3(9))
print(sleepy3(3))
print(sleepy3(2))
print(sleepy3(1))
print(sleepy3(1))