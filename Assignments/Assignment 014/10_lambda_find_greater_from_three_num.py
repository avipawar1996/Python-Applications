# Question: Write a lambda function which accepts three numbers and returns the maximum number.

# Solution:
# ------------------------------------------------------

FindGreaterNum = lambda num1, num2, num3: ("All numbers are same." if num1 == num2 == num3 else (num1 if num1 > num2 and num1 >= num3 else (num2 if num2 >= num1 and num2 >= num3 else num3)))

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    big_num = FindGreaterNum(num1, num2, num3)

    if(isinstance(big_num, str)):
        print(big_num)

    else:
        print(big_num, "is greater number among", num1, num2, num3)
        
if(__name__ == "__main__"):
    main()