'''
Question: Write a program which contain lambda function which accept one number and return the power of two

Input: 4        Output: 16
Input: 6        Output: 36

'''

CalcPowerTwo = lambda num, pwr = 2 : num ** 2

def main():
    num = int(input("Enter the number: "))
    sqOfNum = CalcPowerTwo(num)
    print(f"2 power of {num} is:  {sqOfNum}")

if __name__ == "__main__":
    main()