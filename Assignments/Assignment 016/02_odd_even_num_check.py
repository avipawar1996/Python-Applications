# Question: Write a program which contains one function named as ChkFun() which accept one parameter as number. If number is even then it should display "Even Number" otherwisr display "Odd Number" on console

# Input: 11       Output: Odd Number
# Input: 8        Output: Even Number

# Solution:->
# --------------------------------------------------------------------------------

# def ChkNum(num): return "Even Number" if num % 2 == 0 else "Odd Number"
ChkNum = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"

def main(): print(ChkNum(int(input("Enter the number: "))))

if(__name__ == "__main__"): main()