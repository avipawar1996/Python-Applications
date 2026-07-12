'''
Write a python program using multiprocessing.Pool() to calculate count of all odd numbers from 1 to N for every number from given list.

Input: Data = [1000000, 2000000, 3000000, 4000000]

Expected output Format:
Process ID: 
Input Number:
Odd Numbers Count:


'''
import multiprocessing
import os

def CalcCountOfOddNumUptoN(num):
    count = 0
    for i in range(1, num+1, 2):
        count = count + 1
    return (count, os.getpid())

def main():
    list_size = int(input("Enter the size of list of numbers: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number: ")))
    
    pobj = multiprocessing.Pool()
    result = pobj.map(CalcCountOfOddNumUptoN, num_list)
    pobj.close()
    pobj.join()

    mapped_res = zip(num_list, result)
    for num, [count, pid] in mapped_res:
        print("-"*40)
        print(f"\n Input Number: {num}\n Count of Odd Numbers upto {num} is: {count}\n Processe ID: {pid}\n")
        print("-"*40)

if(__name__ == "__main__"):
    main()