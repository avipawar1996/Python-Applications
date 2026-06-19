# Question 1:
# What is user defined function? 
# Write a function to accept two numbers and return their multiplication.

# Answer: User defined function is a function written by user that is not from imported modules/libraries
# Below is program to multiplication function that return multiplication of 2 given numbers

def multiplication (num1, num2):
    return num1 * num2

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    mul = multiplication(num1, num2)
    print("Multiplication of", num1, "&", "is:", mul)

if(__name__ == "__main__"):
    main()