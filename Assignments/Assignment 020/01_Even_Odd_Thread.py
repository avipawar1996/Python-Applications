'''
Design a python application which contains two different thread named Even and Odd.

Even thread to display first 10 even numbers.
Odd thread to display first 10 odd numbers.
Both thread should run independently using the threading module.
Ensure proper thread creation and execution.

'''

import threading

def FindFirstNEvenNumber(num):
    for n in (range(2, (num*2)+1, 2)):
        print(n, end="    ")
    print()

def FindFirstNOddNumber(num):
    for n in range(1, (num*2)+1, 2):
        print(n, end="    ")
    print()

def main():
    num = int(input("Enter the number: "))
    t1 = threading.Thread(target=FindFirstNEvenNumber, args=(num,))
    t2 = threading.Thread(target=FindFirstNOddNumber, args=(num,))

    t1.start()
    t2.start()

if (__name__ == "__main__"):
    main()