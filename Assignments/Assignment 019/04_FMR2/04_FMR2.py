'''
Question: Write a program which contain filter(), map() and reduce() in it.
Python application contains one list which contains number accepted from user. Filter should filter out all such numbers which are even. Map function will calculate square of filtered numbers. Reduce reduce() will return the addition of all that numbers

Input List: [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter: [2, 4, 4, 2, 8, 10]
List after map: [4,16, 16, 4, 64, 100]
Output of reduce: 204
'''

from functools import reduce
from Marvellous_num import CalcSum, CalcSquare, checkIsEven

def main():
    no_of_el = int(input("Enter the number of elements to contain in list: "))
    num_list = list()
    for i in range(0, no_of_el):
        num_list.append(int(input("Enter the number: ")))
    
    fltrd_list = list(filter(checkIsEven, num_list))
    print("\n List after filter: ", fltrd_list)

        
    mapped_list = list(map(CalcSquare, fltrd_list))
    print("\n List after Map: ", mapped_list)

    sumOfNum = reduce(CalcSum, mapped_list)
    print("\n Product after Reduce: ", sumOfNum)

if (__name__ == "__main__"):
    main()