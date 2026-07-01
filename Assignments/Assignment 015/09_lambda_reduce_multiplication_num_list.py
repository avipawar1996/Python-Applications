# Question: Write a lambda function using reduce() which accepts a list of numbers and returns product of elements.

# Solution:
# ----------------------------------------------------------------------------------

from functools import reduce

Multiplication = lambda num1, num2 : num1 * num2

def main():
    lst = [11, 21, 31, 41, 51]

    mul = reduce(Multiplication, lst)
    print(mul)

if(__name__ == "__main__"):
    main()