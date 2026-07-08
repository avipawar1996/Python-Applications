'''
Write a program which accepts N numbers from user and store it in the list. Return addition of all elements from that list.
Input: Number of element: 6
Input elements: 13 5 45 7 4 56
Output: 130
'''
from functools import reduce

CalcSum = lambda num1, num2: num1 + num2

def main():
    no_of_elem = int(input("Enter the number of elements: "))
    no_list = list()
    for i in range(1, no_of_elem+1):
        no_list.append(int(input("Enter the number: ")))

    sum_list = reduce(CalcSum, no_list)

    print("Sum of elements: ", sum_list)

if(__name__ == "__main__"):
    main()