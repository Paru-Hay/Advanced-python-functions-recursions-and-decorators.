# 1. decorator_name(func):
# decorator_name: This is the name of the decorator function.
# func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.


# 2. wrapper(*args, **kwargs):
# wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.

# *args: This collects any positional arguments passed to the decorated function into a tuple.

# **kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.

# The wrapper function allows the decorator to handle functions with any number and types of arguments.


# 3. @decorator_name:
# This syntax applies the decorator to the function_to_decorate function.
# It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate).