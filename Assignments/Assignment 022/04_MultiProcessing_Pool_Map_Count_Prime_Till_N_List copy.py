'''
Write a program that calculates 1^5+2^5+3^5+4^5+...+N^5 for multiple values of N simultaneously using Pool

Input Example:
[ 1000000, 2000000, 3000000, 4000000 ]

Measure total execution time.

'''
import multiprocessing
import os
import time

def calculate_x_power_till_n(num):
    print(f"Process {os.getpid()} is handling number: {num}")
    sum = 0
    for i in range(1, num+1):
        sum = sum + (i**5)
    return sum

def main():
    list_size = int(input("Enter the size of list: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number in list: ")))

    started_at = time.perf_counter()

    pobj = multiprocessing.Pool()

    result = list(pobj.map(calculate_x_power_till_n, num_list))

    pobj.close()
    pobj.join()

    ended_at = time.perf_counter()
    exec_time = ended_at - started_at

    result_map = zip(num_list, result)


    for num, sum in result_map:
        print(f"Sum of 5th power of numbers from 1 to {num} =  {sum}")

    print(f"Execution time is: {exec_time}")

if(__name__ == "__main__"):
    main()