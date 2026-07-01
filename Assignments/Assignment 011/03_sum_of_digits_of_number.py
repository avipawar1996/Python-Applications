# Question: -> Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

# Solution:

def calcSumOfDigitsOfNum(num):
    sum = 0
    for i in num:
        sum = sum + int(i)
    return sum

def main():
    num = input("Enter the number: ")
    sum_of_digits = calcSumOfDigitsOfNum(num)
    print("Sum of digits of", num, "is:", sum_of_digits)

if(__name__ == "__main__"):
    main()