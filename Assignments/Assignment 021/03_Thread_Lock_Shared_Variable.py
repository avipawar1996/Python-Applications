'''
Design a python application where multiple threads update a shared variable

Use a lock to avoid race condition
Each thread should increament the shared counter multiple times
Display the final value of counter after all threads completes execution
'''

import threading
lock = threading.Lock()
import time

counter = 0

def IncrementCounterThread1():
    global counter
    for i in range(0, 5):
        with lock:
            counter = counter + 1
            print("Incrementing by Thread1")

def IncrementCounterThread2():
    global counter
    for i in range(0, 5):
        with lock:
            counter = counter + 1
            print("Incrementing by Thread2")

def IncrementCounterThread3():
    global counter
    for i in range(0, 5):
        with lock:
            counter = counter + 1
            print("Incrementing by Thread3")

def IncrementCounterThread4():
    # No locking mechanism i.e. "with lock:"
    global counter
    for i in range(0, 5):
        counter = counter + 1
        print(f"Incrementing by: {threading.current_thread().name}")

def main():
    t1 = threading.Thread(target=IncrementCounterThread1)
    t2 = threading.Thread(target=IncrementCounterThread2)
    t3 = threading.Thread(target=IncrementCounterThread3)

    t4 = threading.Thread(target=IncrementCounterThread4)
    t5 = threading.Thread(target=IncrementCounterThread4)
    t6 = threading.Thread(target=IncrementCounterThread4)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    t4.start()
    t5.start()
    t6.start()

    t4.join()
    t5.join()
    t6.join()

    global counter
    print(f"Counter value with locking mechanism: {counter}")

if (__name__ == "__main__"):
    main()

