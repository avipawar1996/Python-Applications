# Question: -> Write a program which accepts two number and prints addition, substraction, multiplication and division.
# Input: 12
# Output: 1 2 3 4 6 12

# Solution:

def Addition(num1, num2): return num1 + num2
def Substraction(num1, num2): return num1 - num2
def Division(num1, num2): return num1 / num2
def Multiplication(num1, num2): return num1 * num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    sum = Addition(num1, num2)
    sub = Substraction(num1, num2)
    mul = Multiplication(num1, num2)
    div = Division(num1, num2)

    print(num1, "+", num2, "=", sum)
    print(num1, "-", num2, "=", sub)
    print(num1, "*", num2, "=", mul)
    print(num1, "/", num2, "=", div)
    

if(__name__ == "__main__"):
    main()