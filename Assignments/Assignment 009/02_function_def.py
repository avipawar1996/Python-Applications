# Question:-> Write a program which contains one function ChkGreater() that accepts two numbers and print greater number.
# Input: 10 20
# Output: 20 is greater

# Solution:->

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    bigNo = ChkGreater(num1, num2)

    if(isinstance(bigNo, str)):
        print(bigNo)
    else:
        print(bigNo, "is greater.")

def ChkGreater(num1, num2):
    if(num1 > num2):
        return num1
    elif (num1 == num2):
        return "Both numbers are equal."
    else:
        return num2
    
if(__name__ == "__main__"):
    main()