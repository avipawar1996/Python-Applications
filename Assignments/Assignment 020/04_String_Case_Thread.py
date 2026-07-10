'''
Design a python application that creates three threads named Small, Capital and Digit.

    All thread should accept string as input
    Small thread should count and display number of lower case characters
    Capital thread should count and display number of upper case characters
    Digit thread should count and display number of numeric digit characters

    Each thread must also display:
        Thread ID
        Thread Name
'''

import threading

def CalcLowerInStr(user_str):
    count = 0
    for char in user_str:
        if(char >= "a" and char <= "z"):
            count = count + 1
    print(f"Number of lower case characters in given string: {count}")
    print("Thread Name: ", threading.current_thread().name)
    print("Thread ID: ", threading.get_ident())

def CalcUpperInStr(user_str):
    count = 0
    for char in user_str:
        if(char >= "A" and char <= "Z"):
            count = count + 1
    print(f"Number of upper case characters in given string: {count}")
    print("Thread Name: ", threading.current_thread().name)
    print("Thread ID: ", threading.get_ident())


def CalcDigitsInStr(user_str):
    count = 0
    for char in user_str:
        if(char >= "0" and char <= "9"):
            count = count + 1
    print(f"Number of numeric characters in given string: {count}")
    print("Thread Name: ", threading.current_thread().name)
    print("Thread ID: ", threading.get_ident())
 
def main():
    user_str = input("Enter your string: ")

    t_lower = threading.Thread(target=CalcLowerInStr, args=(user_str,))
    t_upper = threading.Thread(target=CalcUpperInStr, args=(user_str,))
    t_digit = threading.Thread(target=CalcDigitsInStr, args=(user_str,))

    t_lower.start()
    t_upper.start()
    t_digit.start()

    t_lower.join()
    t_upper.join()
    t_digit.join()

    print("Thread Name: ", threading.current_thread().name)
    print("Thread ID: ", threading.get_ident())
if(__name__ == "__main__"):
    main()