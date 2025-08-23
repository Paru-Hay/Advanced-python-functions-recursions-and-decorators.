# n Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.
# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
# Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

# 1 Basic decorator example.
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()

# 2 Decorator with parameters.
def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))

# Refer to explanation of parameter.py for detailed explanation of parameters used in decorators.

# 3 Functions as first-class objects.
# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet  # Assign the greet function to say_hi
print(say_hi("Alice")) 

# Passing a function as an argument
def apply(f, v):
    return f(v)
res = apply(say_hi, "Bob")
print(res) 

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))

# Role of First-Class Functions in Decorators
# Decorators take a function as input to modify or enhance its behavior.
# They return a new function that wraps the original, adding behavior before or after execution.
# The original function is replaced by decorated function when assigned to same name.

