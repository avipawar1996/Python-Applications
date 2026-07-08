'''
Write a program which accepts N numbers from user and store it in the list. Return the maximum number from that list. Main python file accept N numbers from user and pass each number to chkPrime() function which is part our user defined module named as MarvellousNum.py Name of the function from main python file should be ListPrime().

Input: Number of element: 11
Input elements: 13 5 45 7 4 56 10 34 2 5 8
Output: 54(13 + 5 + 7 + 2 + 5)
'''

from MarvellousNum import ChkPrime, Addition
from functools import reduce

def ListPrime(num_list):
    list_prime = list()
    for num in num_list: 
        if(ChkPrime(num)):
            list_prime.append(num)
    return list_prime

def main():
    no_of_elem = int(input("Enter the number of elements: "))
    no_list = list()
    for i in range(1, no_of_elem+1):
        no_list.append(int(input("Enter the number: ")))
    
    prime_list = list(ListPrime(no_list))
    print("Prime list: ", prime_list)
    sum_prime_num = reduce(Addition, prime_list)

    print(f"Sum of prime numbers from given list is {sum_prime_num}")


if(__name__ == "__main__"):
    main()