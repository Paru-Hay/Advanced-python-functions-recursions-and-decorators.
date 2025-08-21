# The special syntax *args in function definitions is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. These arguments are grouped into a tuple, allowing the function to handle any number of inputs.
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GitHub')

# Example 2: *args with a first extra argument.
def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)

fun('Hello', 'Welcome', 'to', 'GitHub')