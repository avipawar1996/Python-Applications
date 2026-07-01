# Question: Write a lambda function which accepts one number and returns  True if number is even otherwise False.

# Solution:
# ---------------------------------------------------------------------------

CheckIfEven = lambda num: True if (num % 2 == 0) else False

def main():
    num = int(input("Enter the Number: "))
    isEven = CheckIfEven(num)

    if(isEven):
        print(num, "is Even Number.")
    else:
        print(num, "is Odd Number.")
        
if(__name__ == "__main__"):
    main()