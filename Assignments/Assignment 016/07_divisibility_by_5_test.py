# Question: Write a program which accepts one number from user and returns True if number is divisible by 5 otherwise return False.

# Input: 8          Output: False
# Input: 25         Output: True

# Solution: 
# ---------------------------------------------------------------------------------------

CheckDivisibility = lambda dividend, divisor: True if dividend % divisor == 0 else False

# def CheckDivisibility(dividend, divisor):
#     return True if dividend % divisor == 0 else False

def main():
    divident = int(input("Enter the dividend number (Number To be divided): "))
    divisor = int(input(("Enter the divisor number (Number To be divided by): ")))
    divisibility_test_res = CheckDivisibility(dividend=divident, divisor=divisor)
    print(divisibility_test_res)

if(__name__ == "__main__"):
    main()
