# A recursive function is just like any other Python function except that it calls itself in its body.
# Base Case: The stopping condition that prevents infinite recursion.
# Recursive Case: The part of the function where it calls itself with modified parameters.

# Factorial calculation
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1) 
    
print(factorial(5)) 

