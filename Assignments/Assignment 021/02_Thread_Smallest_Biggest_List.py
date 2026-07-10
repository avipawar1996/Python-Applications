'''
Design a python application that creates two threads.

Thread1 should should display maximum number from a list
Thread2 should should display minimum number from the same list
The list should be accepted from the user

'''

import threading

CompareNum = lambda num1, num2, isBigger : num1 > num2 if isBigger else num1 < num2

def get_smallest_num(num_list):
    small_num = num_list[0]
    for i in range(1, len(num_list)):
        if(CompareNum(num_list[i], small_num, False)):
            small_num = num_list[i]
    print("small_num: ", small_num)
    
def get_biggest_num(num_list):
    big_num = num_list[0]
    for i in range(1, len(num_list)):
        if(CompareNum(num_list[i], big_num, True)):
            big_num = num_list[i]
    print("big_num: ", big_num)

def main():
    num = int(input("Enter the number of elements you want in list: "))
    num_list = list()
    for i in range(num):
        num_list.append(int(input("Enter the number: ")))

    t_big_num = threading.Thread(target=get_biggest_num, args=(num_list,))
    t_small_num = threading.Thread(target=get_smallest_num, args=(num_list,))

    t_big_num.start()
    t_small_num.start()

    t_big_num.join()
    t_small_num.join()

if(__name__ == "__main__"):
    main()