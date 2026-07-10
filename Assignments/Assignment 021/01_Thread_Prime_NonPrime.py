'''
Design a python application that creates two threads named Prime and NonPrime.

Both thread should accept a list of integer
Prime Thread should display all prime numbers from list
NonPrime Thread should display all non-prime numbers from list

'''

import threading

def chkPrime(num):
    for i in range(2, int(num/2)+1):
        if(num%i == 0):
            return False
    return True

def get_prime_num(num_list):
    print("Prime Numbers from given list: ", end="")
    prime_list = list()
    for num in num_list:
        if(chkPrime(num)):
            prime_list.append(num)
    for num in prime_list:
        print(num, end="    ")
    print()

def get_non_prime_num(num_list):
    non_prime_list = list()
    print("Non Prime Numbers from given list: ", end="")
    for num in num_list:
        if(chkPrime(num) == False):
            non_prime_list.append(num)
    for num in non_prime_list:
        print(num, end="    ")
    print()

def main():
    num = int(input("Enter the number of elements you want in list: "))
    num_list = list()
    for i in range(num):
        num_list.append(int(input("Enter the number: ")))

    t_prime = threading.Thread(target=get_prime_num, args=(num_list,))
    t_non_prime = threading.Thread(target=get_non_prime_num, args=(num_list,))

    t_non_prime.start()
    t_prime.start()

if(__name__ == "__main__"):
    main()