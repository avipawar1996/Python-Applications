'''
Design a python application that creates two threads named Thread1 and Thread2.
    Thread1 to display numbers from 1 to 50
    Thread2 to display numbers from 50 to 1 in reverse order

    Ensure that:
        Thread2 to start execution only after completion of Thread1

    User appropriate thread synchronization
'''
import threading

def PrintForwardNum(num):
    for i in range(1, num+1):
        print(i, end="  ")
    print()

def PrintReverseNum(num):
    for i in range(1, (num+1)):
        print((num+1) - i, end="  ")
    print()

def main():
    num = int(input("Enter the number: "))

    t1 = threading.Thread(target=PrintForwardNum, args=(num,))
    t2 = threading.Thread(target=PrintReverseNum, args=(num,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if(__name__ == "__main__"):
    main()