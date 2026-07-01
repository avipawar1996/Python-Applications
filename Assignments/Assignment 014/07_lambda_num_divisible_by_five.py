# Question: Write a lambda function which accepts one number and returns  True if number is divisible by 5.

# Solution:
# ---------------------------------------------------------------------------

CheckIfDivisibleByFive = lambda num: True if (num % 5 == 0) else False

def main():
    num = int(input("Enter the Number: "))
    isDivisibleByFive = CheckIfDivisibleByFive(num)

    if(isDivisibleByFive):
        print(num, "is divisible by 5")
    else:
        print(num, "is NOT divisible by 5")
        
if(__name__ == "__main__"):
    main()