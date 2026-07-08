'''
Question: Write a program to display following pattern by accepting number from user.
Input: 5

*    *    *    *    *     
*    *    *    *     
*    *    *    
*    *    
*   

''' 
# Solution :-> -----------------------------------------------------

def printPattern(num):
    for i in range (num):
        for i in range (num-i):
            print("*", end="    ")
        print()

def main():
    num_of_cols_rows = int(input("Enter the number of lines and columns to print '*': "))
    printPattern(num_of_cols_rows)

if(__name__ == "__main__"):
    main()