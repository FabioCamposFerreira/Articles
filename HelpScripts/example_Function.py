# Python 3
# Author: Fábio Campos
 
# function
def func(x):
    print("x is "+str(x))
    return True

print("func(21) = "+str(func(21)))

# *args and **kargs
def func2(*args, **kargs):
    print("*args = "+str(*args))
    print("*kargs = "+str(*kargs))
func2("one", "two", "three", "a":1, "b":2, "c":3)