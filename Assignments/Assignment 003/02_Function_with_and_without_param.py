# Question 2:
# What is difference between:
# 1. Function with parameter        2. Function without parameter
# Give one example of each

# Solution:
# Any function that accept input during function call is function with parameter and function that does not take any parameter while calling it, is a non-parameterised function

# Function without parameter:
def greet():
    print("Hello,", input("Please enter user name: "))

# Function with parameter:
def greeting(user_name):
    print("Hello,", user_name)

def main():
    greet() # Calling without parameter
    greeting(input("Enter user name: ")) # Calling with Parameter

if(__name__ == "__main__"):
    main()