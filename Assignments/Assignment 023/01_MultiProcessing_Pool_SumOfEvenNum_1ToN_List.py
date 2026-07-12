'''
Write a python program using multiprocessing.Pool() to calculate sum of all even numbers from 1 to N for every number from given list.

Input: Data = [1000000, 2000000, 3000000, 4000000]

Expected task:
For each number N, calculate:
2 + 4 + 6 + 8 + .. N

Expected output Format:
Process ID: 
Input Number:
Sum of Even Numbers upto:

'''
import multiprocessing
import os

def CalcSumOfEvenNumUptoN(num):
    sum = 0
    for i in range(2, num+1, 2):
        sum = sum + i
    return (sum, os.getpid())

def main():
    list_size = int(input("Enter the size of list of numbers: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number: ")))
    
    pobj = multiprocessing.Pool()
    result = pobj.map(CalcSumOfEvenNumUptoN, num_list)
    pobj.close()
    pobj.join()

    mapped_res = zip(num_list, result)
    for num, [sum, pid] in mapped_res:
        print("-"*40)
        print(f"\n Input Number: {num}\n Sum of even numbers upto {num}: {sum}\n Processe ID: {pid}\n")
        print("-"*40)

if(__name__ == "__main__"):
    main()