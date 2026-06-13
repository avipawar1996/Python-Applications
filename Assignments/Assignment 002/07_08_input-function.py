# Question 07:
# Why input() return a string and how to convert it?

# Solution: 
# Input function takes input in form of characters from keyboard and form a string of it
# convert into other form:
age = input("Enter your age: ") #take user input from keyboard
age = int(age) # convert string returned by input() to int
# age = int(input("Enter your age: ")) # Simple and short

# -----------------------------------------------------------------------------

# Question 08:
# Predict the output
# x = input("Enter the number: ")
# print(type(x))
# Explain why so.

# Solution:
# Output: <class 'str'>
x = input("Enter the number: ")
print(type(x))
# Explaination: input() functionn returns the string of values entered on keyboard, so the type is text i.e. 'str' class object