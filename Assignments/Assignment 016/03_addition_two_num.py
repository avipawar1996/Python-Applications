# Question: Write a program which contains one function named as Add() which accept two numbers from user and return addition of that two numbers.
 
# Input: 11    5      Output: 16

# Solution:->
# --------------------------------------------------------------------------------

from functools import reduce
Add = lambda num1, num2: num1 + num2
# def Add(num1, num2): return num1 + num2

def main():
    n = int(input("How many numbers to be added? "))
    num_lst = list()
    for i in range(n):
        num_lst.append(int(input("Enter number: ")))

    sum = reduce(Add, num_lst)
    print(sum)

# def main():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     sum = Add(num1, num2)
#     print(num1, "+", num2, "=", sum)

if(__name__ == "__main__"): main()