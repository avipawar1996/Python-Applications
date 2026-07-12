'''
Wirte a program that accepts list of integers and uses pool.map() to calculate the sum of squares from 1 to N for every element in the list.

Example Input: [1000000, 2000000, 3000000, 4000000]
Expected Output: [333333383333335000000, 2666666866666670000000, 9000000450000005000000, 21333334133333340000000]
'''

import multiprocessing
import os

def CalcSquareSumUptoN(num):

    print(f"worker pid is: {os.getpid()} ------------- worker ppid is: {os.getppid()}")
    sum = 0
    for i in range(1, num+1):
        sum = sum + i**2
    return sum


def main():
    list_size = int(input("Enter the size of list: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number in list: ")))
    print(f"Entered list of numbers: {num_list}")

    p1Obj =  multiprocessing.Pool()
    SquareSumTillN_list = p1Obj.map(CalcSquareSumUptoN, num_list)
    p1Obj.close()
    p1Obj.join()

    print(f"Result is: {SquareSumTillN_list}")
    print(f"in main pid is: {os.getpid()} -------------in main ppid is: {os.getppid()}")

if(__name__ == "__main__"):
    main()