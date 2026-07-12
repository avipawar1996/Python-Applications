'''
For every number in the given list, count how many prime numbers exists between 1 to N using multiprocessing pool.

Example:
10000
20000
30000
40000

Display total number of prime count for each number.

'''
import multiprocessing
import os

def check_n_prime_num(num):
    print(f"Process {os.getpid()} is handling number: {num}")
    count = 0
    for n in range (2, num+1):
        isPrime: bool = True
        for i in range(2, int(n/2)+1):
            if(n % i == 0):
                isPrime = False
                break
        if isPrime: 
            count = count + 1

    return count

def main():
    list_size = int(input("Enter the size of list: "))
    num_list = list()
    for i in range(list_size):
        num_list.append(int(input("Enter the number in list: ")))

    pobj = multiprocessing.Pool()
    result = list(pobj.map(check_n_prime_num, num_list))

    result_map = zip(num_list, result)

    for num, count in result_map:
        print(f"Count of Primary Numbers upto {num}: {count}")

if(__name__ == "__main__"):
    main()