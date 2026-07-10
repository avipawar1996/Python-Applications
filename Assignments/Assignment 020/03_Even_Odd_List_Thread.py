'''
Design a python application which contains two different thread named EvenList and OddList.

Both thread should accept one integer number as a parameter

The EvenList should:
    Extract all even element from the list
    Calculate and Display their sum

The OddList should:
    Extract all odd elements from the list
    Calculate and Display their sum

Threads should run concurrently.

'''
import threading
from functools import reduce

Addition = lambda num1, num2 : num1 + num2

def GetNumList(num):
    num_list = list()
    for i in range(0, num):
        num_list.append(int(input("Enter the number: ")))
    return num_list

def EvenSum(num_list):
    even_list = list(filter(lambda num: num%2 == 0, num_list))
    if(len(even_list)):
        sum_of_even_list = (reduce(Addition, even_list))
    print(f"sum_of_even_list: {sum_of_even_list}")

def OddSum(num_list):
    odd_list = list(filter(lambda num: num%2 != 0, num_list))
    if(len(odd_list)):
        sum_of_odd_list = reduce(Addition, odd_list)
    print(f"sum_of_odd_list: {sum_of_odd_list}")

def main():
    num = int(input("Enter the number: "))
    num_list = GetNumList(num)
    t_even = threading.Thread(target=EvenSum, args=(num_list,))
    t_odd = threading.Thread(target=OddSum, args=(num_list,))

    t_even.start()
    t_odd.start()
    t_even.join()
    t_odd.join()
    
if (__name__ == "__main__"):
    main()