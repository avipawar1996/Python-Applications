# Question: Write a program which accepts number from user and check whether that number us positive or negative or zero.

# Input: 11             Output: Positive Number
# Input: -8             Output: Negative Number
# Input:  0             Output: Zero

# Solution:->
# --------------------------------------------------------------------------------

CheckNumPolarity = lambda num : "Zero" if num == 0 else ("Positive Number" if num > 0 else "Negative Number")
# def CheckNumPolarity(num): return "Zero" if num == 0 else ("Positive Number" if num > 0 else "Negative Number")

def main():
    num = int(input("Enter the Number: "))
    num_check_res = CheckNumPolarity(num)
    print(num_check_res)

if(__name__ == "__main__"):
    main()