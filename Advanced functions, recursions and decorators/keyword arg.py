# The special syntax **kwargs in function definitions is used to pass a variable length argument list. We use the name kwargs with the double star **.

# A keyword argument is where you provide a name to the variable as you pass it into the function.
# It collects all the additional keyword arguments passed to the function and stores them in a dictionary.

def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))

# Driver code
fun(s1='Welcome', s2='to', s3='GitHub')

# Example 2
def fun(arg1, **kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))

# Driver code
fun("Hi", s1='Welcome', s2='to', s3='GitHub')