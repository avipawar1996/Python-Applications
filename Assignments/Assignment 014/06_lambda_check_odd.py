# Question: Write a lambda function which accepts one number and returns  True if number is Odd otherwise False.

# Solution:
# ---------------------------------------------------------------------------

CheckIfOdd = lambda num: True if (num % 2 != 0) else False

def main():
    num = int(input("Enter the Number: "))
    isOdd = CheckIfOdd(num)

    if(isOdd):
        print(num, "is Odd Number.")
    else:
        print(num, "is Even Number.")
        
if(__name__ == "__main__"):
    main()