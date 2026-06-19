# Question: Write a function that does not return anything but prints a message.
# Explain the default return value of such function.

# Solution:

def addNumbers(num1, num2):
    ans = num1 + num2
    print("Addition of", num1, "&", num2, "is:", ans)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return_value = addNumbers(num1, num2)
    print("Default return value of function: ", return_value)
    print("Default return type of function: ", type(return_value))

if(__name__ == "__main__"):
    main()

# Explaination: Default return value of a function is "None" and the type is "<class "NoneType">