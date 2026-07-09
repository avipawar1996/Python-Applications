'''
Question: Write a program which contain filter(), map() and reduce() in it.
Python application contains one list which contains number accepted from user. Filter should filter out all such numbers which are prime numbers. Map function will multiply each number by 2. Reduce reduce() will return the maximum numbers from all that numbers.

Input List: [2, 70, 11, 10, 17, 23,31,77]
List after filter: [2, 11, 17, 23, 31]
List after map: [4, 22, 34, 46, 62]
Output of reduce: 62
'''

from functools import reduce
from Marvellous_num import MakeNumDbl, checkIfPrime, CompareNum

def main():
    no_of_el = int(input("Enter the number of elements to contain in list: "))
    num_list = list()
    for i in range(0, no_of_el):
        num_list.append(int(input("Enter the number: ")))
    
    fltrd_list = list(filter(checkIfPrime, num_list))
    print("\n List after filter: ", fltrd_list)

        
    mapped_list = list(map(MakeNumDbl, fltrd_list))
    print("\n List after Map: ", mapped_list)

    sumOfNum = reduce(CompareNum, mapped_list)
    print("\n Product after Reduce: ", sumOfNum)

if (__name__ == "__main__"):
    main()