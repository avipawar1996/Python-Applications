'''
Write a program which accepts N numbers from user and store it in the list. Return the maximum number from that list. Accept one more number from user and return the frequency of that number in list.
Input: Number of element: 11
Input elements: 13 5 45 7 4 56 5 34 2 5 65
Element to search: 5
Output: 3
'''
GetFreqOfElem = lambda num_list, num : list(num_list).count(num)

def main():
    no_of_elem = int(input("Enter the number of elements: "))
    no_list = list()
    for i in range(1, no_of_elem+1):
        no_list.append(int(input("Enter the number: ")))

    small_num = GetFreqOfElem(no_list, int(input("Enter the number to be searched: ")))

    print("Smallest number from the list is: ", small_num)

if(__name__ == "__main__"):
    main()