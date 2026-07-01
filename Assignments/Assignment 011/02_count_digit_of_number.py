# Question: -> Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

# Solution:

def calcNumOfDigits(num):
    return len(str(num))

def main():
    num = input("Enter the number: ")
    totalDigitsCount = calcNumOfDigits(num)
    print("Number of digits in", num, ":", totalDigitsCount)

if(__name__ == "__main__"):
    main()