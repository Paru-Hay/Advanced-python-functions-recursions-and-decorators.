# lambda keyword is used to define an anonymous function in Python. 
s1 = 'VS Code'

s2 = lambda func: func.upper()
print(s2(s1))

# 1. Lambda function with condition checking.
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(10))
print(n(-5))
print(n(0))

# 2. Lambda with list comprehension.
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# 3. Lambda with if-else.
check = lambda x: "Even" if x%2 == 0 else "Odd"
print(check(4))
print(check(7))

# 4 . Lambda with multiple statements.
calc = lambda x, y: (x+y, x*y)
res = calc(5, 10)
print(res)

# 5 Lambda with filter.
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x: x%2 == 0, n)
print(list(even))

# 6 Lambda with map. (The map() function in Python takes in a function and a list as an argument)
n = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, n)
print(list(b))

# 7. Lambda with reduce.
from functools import reduce
n = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, n)
print(b)