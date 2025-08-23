# The filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition. It works by applying a function to each element and keeping only those for which function returns True.

# 1 Basic usage of filter() function.
def even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
b = filter(even, numbers)
print(list(b))  

# 2 Using lambda function with filter() ---> This makes the code shorter and easier.
numbers = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, numbers)
print(list(b))

# 3 Filtering and transforming data.
numbers = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, numbers)
c = map(lambda x: x * 2, b)
print(list(c))

# 4 Filtering strings based on length.
words = ['apple', 'banana', 'kiwi', 'cherry', 'fig']
b = filter(lambda x: len(x) > 4, words)
print(list(b))

# 5 Filtering out None values from a list.
data = [0, 1, None, 2, '', 3, 'Hello', [], 4]
b = filter(None, data)
print(list(b))