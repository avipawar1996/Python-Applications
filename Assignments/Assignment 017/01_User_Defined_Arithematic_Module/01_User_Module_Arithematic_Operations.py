# Question: Create one module named Arithematic which contains 4 functions as Add(), Sub(), Mul() and Div(). All functions accepts two numbers as parameter and performs the operation. Write one python program which call all the functions from Arithematic module by accepting the parameters from user.

# Solution:->
# -----------------------------------------------------------------------
from Arithematic import Add, Sub, Mul, Div

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    summation = Add(num1, num2)
    substraction = Sub(num1, num2)
    multiplication = Mul(num1, num2)
    division = Div(num1, num2)

    print(f"{num1} + {num2} = {summation}")
    print(f"{num1} - {num2} = {substraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

if(__name__ == "__main__"):
    main()