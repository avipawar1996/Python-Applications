# Question: Write a lambda function using reduce() which accepts a list of numbers and returns maximum element.

# Solution:
# ----------------------------------------------------------------------------------

from functools import reduce

CheckBigger = lambda num1, num2 : num1 if num1 > num2 else num2

def main():
    lst = [11, 21, 31, 41, 51]

    bigNum = reduce(CheckBigger, lst)
    print(bigNum)

if(__name__ == "__main__"):
    main()