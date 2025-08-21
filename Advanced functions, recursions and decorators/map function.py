# map() function in Python is used to apply a specific function to each element of an iterable (like a list, tuple, or set) and returns a map object (which is an iterator).
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))