# Question 3:
# Predict the output:

# def fun():
#     x = 10
#     print(x)

# fun()
# print(x)

# Explain the reason.

# Solution: 
# Since the variable "x" is used in print function to be printed on console, the variable is not declared and initiated prior the print statement and the one that is defined inside function is limited with the scope of function body hence this will throw error

def fun():
    x = 10
    print(x)

fun()
# print(x) # This statement throws error as x is not defined for this scope.