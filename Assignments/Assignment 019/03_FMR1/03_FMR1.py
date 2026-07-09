'''
Question: Write a program which contain filter(), map() and reduce() in it.
Python application contains one list which contains number accepted from user. Filter should filter out all such numbers which are greater or equals 70 and less than or equal to 90. Map function will increase each number by 10. Reduce reduce() will return the product of all that numbers

Input List: [4, 36, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Filtered List: [76, 89, 86, 90, 70]
Mapped List: [86, 99, 96, 100, 80]
Output of reduce: 6539752000
'''

from functools import reduce
from Marvellous_num import CalcMul, CalcSum, CheckNumInRange

def main():
    no_of_el = int(input("Enter the number of elements to contain in list: "))
    num_list = list()
    for i in range(0, no_of_el):
        num_list.append(int(input("Enter the number: ")))
    
    fltrd_list = list(filter(CheckNumInRange, num_list))
    print("\n List after filter: ", fltrd_list)

        
    mapped_list = list(map(CalcSum, fltrd_list))
    print("\n List after Map: ", mapped_list)

    prodOfNum = reduce(CalcMul, mapped_list)
    print("\n Product after Reduce: ", prodOfNum)

if (__name__ == "__main__"):
    main()