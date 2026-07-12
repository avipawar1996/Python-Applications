'''
Write a program that calculates factorial of multiple numbers simultaneously using multiprocess.Pool().map()

Input: [10, 15, 20, 25]

Display:
    Process ID
    Input Number
    Factorial
'''
import multiprocessing
import os

def FindFactorials(num):
    factorial_of_num = 1
    for i in range(1, num+1):
        factorial_of_num = factorial_of_num * i
    return (num, factorial_of_num, os.getpid())

def main():
    list_size = int(input("Enter the size of list: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number in list: ")))
    print(f"Entered list of numbers: {num_list}")

    p1obj = multiprocessing.Pool()
    result = p1obj.map(FindFactorials, num_list, 1)
    for num, factorial_of_num, PID in result:
        print("Number: ", num)
        print("factorial_of_num: ", factorial_of_num)
        print("PID: ", PID)
    
    p1obj.close()
    p1obj.join()

if(__name__ == "__main__"):
    main()