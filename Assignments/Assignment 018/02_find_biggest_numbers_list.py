'''
Write a program which accepts N numbers from user and store it in the list. Return the maximum number from that list.
Input: Number of element: 6
Input elements: 13 5 45 7 4 56
Output: 56
'''
from functools import reduce

FindBiggestNum = lambda num1, num2: num1 if num1 > num2 else num2

def main():
    no_of_elem = int(input("Enter the number of elements: "))
    no_list = list()
    for i in range(1, no_of_elem+1):
        no_list.append(int(input("Enter the number: ")))

    big_num = reduce(FindBiggestNum, no_list)

    print("Biggest number from the list is: ", big_num)

if(__name__ == "__main__"):
    main()