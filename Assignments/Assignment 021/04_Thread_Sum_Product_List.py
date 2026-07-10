'''
Design a python application that creates two threads.

Thread1 should compute sum of all the elements from the list
Thread2 should compute product of all the elements from the list
Return the results to main thread and display them.

'''

import threading
import queue
from functools import reduce

q = queue.Queue()

def Addition(num_list, q):
    q.put(("sum",  reduce(lambda num1, num2: num1+num2, num_list)))

def Multiplication(num_list, q):
    q.put(("mul",  reduce(lambda num1, num2: num1*num2, num_list)))

def main():
    num = int(input("Enter the list size: "))
    num_list = list()
    for i in range(num):
        num_list.append(int(input("Enter the number: ")))
    
    t_add = threading.Thread(target=Addition, args=(num_list, q,))
    t_prod = threading.Thread(target=Multiplication, args=(num_list, q,))

    t_add.start()
    t_prod.start()

    t_add.join()
    t_prod.join()

    result = {}

    while (not q.empty()):
        key, value = q.get()
        result[key] = value

    print("Addition of numbers: ", result['sum'])
    print("Multiplication of numbers: ", result['mul'])

if(__name__ == "__main__"):
    main()