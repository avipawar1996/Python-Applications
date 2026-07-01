# Question: -> Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

# Solution:
# ----------------------------------------------------------------------------

# from functools import reduce
# Addition = lambda num1, num2 : num1 + num2

def CheckIfPerfectNumber(num):
    factors_of_num = list()
    for r in range(1, int(num/2)+1):
        if(num % r == 0):
            factors_of_num.append(r)
    print(factors_of_num)
    
    for f in factors_of_num:
        f_sum = f_sum + f
    return f_sum == num
    
    # return reduce(Addition, factors_of_num) == num

def main():
    num = int(input("Enter the number: "))

    isPerfectNum = CheckIfPerfectNumber(num)
    if(isPerfectNum):
        print(num, "is Perfect Number")
    else:
        print(num, "is NOT Perfect Number")

if(__name__ == "__main__"):
    main()