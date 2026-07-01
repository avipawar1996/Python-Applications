# Question: Write a lambda function which accepts two numbers and returns the smaller number.

# Solution:
# ------------------------------------------------------

FindSmallerNum = lambda num1, num2: num2 if num1 > num2 else (num1 if num2 > num1 else "Numbers are same.")

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    smaller_num = FindSmallerNum(num1, num2)

    if(isinstance(smaller_num, str)):
        print(smaller_num)

    else:
        print(smaller_num, "is smaller number among", num1, num2)
        
if(__name__ == "__main__"):
    main()