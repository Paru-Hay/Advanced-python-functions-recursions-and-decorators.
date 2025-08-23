# 1. Function Decorators:
# A function decorator is a function that takes another function as an argument, extends its behavior without explicitly modifying it, and returns a new function.
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet()

# 2 Method Decorators:
# A method decorator is similar to a function decorator but is specifically designed to work with methods within classes. It takes a method as an argument, extends its behavior, and returns a new method.
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# 3 Class Decorators:
# A class decorator is a function that takes a class as an argument, extends or modifies its
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)