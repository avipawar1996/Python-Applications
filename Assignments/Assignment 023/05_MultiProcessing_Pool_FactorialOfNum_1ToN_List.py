'''
Write a python program that calculate the factorials of multiple numbers simultaneously using multiprocessing.Pool()

Input: [10, 15, 20, 25]

Expected task: For every N, calculate N!

Expected output Format:
Process ID: 
Input Number:
Factorial of Number: 


'''
import multiprocessing
import os

import sys
sys.set_int_max_str_digits(1000000000)

def CalcFactorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial = factorial * i
    return (num, factorial, os.getpid())

def main():
    list_size = int(input("Enter the size of list of numbers: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number: ")))
    
    pobj = multiprocessing.Pool()
    result = pobj.map(CalcFactorial, num_list)
    pobj.close()
    pobj.join()

    for num, factorial, pid in result:
        print("-"*40)
        print(f"\n Input Number: {num}\n Factorial of Number {num}: {factorial}\n Processe ID: {pid}\n")
        print("-"*40)

if(__name__ == "__main__"):
    main()