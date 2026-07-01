# Question: Write a lambda function which accepts two numbers and returns the maximum number.

# Solution:
# ------------------------------------------------------

FindGreaterNum = lambda num1, num2: num1 if num1 > num2 else (num2 if num2 > num1 else "Numbers are same.")

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    big_num = FindGreaterNum(num1, num2)

    if(isinstance(big_num, str)):
        print(big_num)

    else:
        print(big_num, "is greater number among", num1, num2)
        
if(__name__ == "__main__"):
    main()