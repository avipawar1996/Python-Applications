'''
Design a python application which contains two different thread named EvenFactor and OddFactor.

Both thread should accept one integer number as a parameter

The EvenFactor should:
    Identify all even factors of given number
    Calculate and Display sum of the even factors numbers

The OddFactor should:
    Identify all odd factors of given number
    Calculate and Display sum of the odd factors numbers

After these threads completion, main thread should display message "Exit from Main"

'''

import threading
from functools import reduce

def GetFactors(num):
    fact_list = list()
    for i in range(1, int(num+1/2)+1):
        if num%i == 0:
            fact_list.append(i) 
    return fact_list

Addition = lambda num1, num2 : num1 + num2

def EvenFactorsSum(fact_list):
    even_factors = list(filter(lambda num: num%2 == 0, fact_list))

    if(len(even_factors)):
        sum_of_even_factors = (reduce(Addition, even_factors))

    print(f"sum_of_odd_factors: {sum_of_even_factors}")

def OddFactorsSum(fact_list):
    odd_factors = list(filter(lambda num: num%2 != 0, fact_list))

    if(len(odd_factors)):
        sum_of_odd_factors = reduce(Addition, odd_factors)

    print(f"sum_of_odd_factors: {sum_of_odd_factors}")

def main():
    num = int(input("Enter the number: "))
    fact_of_num = GetFactors(num)

    t_even = threading.Thread(target=EvenFactorsSum, args=(fact_of_num,))
    t_odd = threading.Thread(target=OddFactorsSum, args=(fact_of_num,))

    t_even.start()
    t_even.join()
    t_odd.start()
    t_odd.join()
    print("Exit from main")

    t_main = threading.main_thread()
    print(threading.get_ident())
if (__name__ == "__main__"):
    main()