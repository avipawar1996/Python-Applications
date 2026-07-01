# Question: Write a lambda function using reduce() which accepts a list of numbers and returns addition of numbers

# Solution:
# ----------------------------------------------------------------------------------

from functools import reduce

Addition = lambda num1, num2 : num1 + num2

def main():
    lst = [11, 21, 31, 41, 51]

    sum = reduce(Addition, lst)
    print(sum)

if(__name__ == "__main__"):
    main()