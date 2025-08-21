# In Python, *args and **kwargs are used to allow functions to accept an arbitrary number of arguments. These features provide great flexibility when designing functions that need to handle a varying number of inputs.

# *args example
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)