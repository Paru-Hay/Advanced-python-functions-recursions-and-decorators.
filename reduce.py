# The reduce() function in Python applies a given function cumulatively to all items in an iterable, reducing it to a single final value.

# Basic usage.
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4]
result = reduce(add, numbers)
print(result)  

# Using lambda function with reduce() ---> This makes the code shorter and easier.
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)

# 3 Using reduce() with operator module for multiplication.
import functools
import operator
numbers = [1, 2, 3, 4]
print(functools.reduce(operator.mul, numbers))
print(functools.reduce(operator.add, numbers))  
print(functools.reduce(operator.add, ["Python", "is", "fun"]))

# 4 Using initializer.
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers, 10)  # Starts with 10
print(result)

# 5 Difference between reduce() and accumulate().
from itertools import accumulate
from operator import add
numbers = [1, 2, 3, 4]
res = accumulate(numbers, add)
print(list(res))  

