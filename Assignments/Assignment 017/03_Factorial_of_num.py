'''
Question: Write a program which accept one number and return its factorial

Input: 5        Output: 120
'''

# Solution :-> ------------------------------------------------------------

def CalcFactorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter the number: "))
    fact = CalcFactorial(num)
    print(f"factorial of {num} : {fact}")

if(__name__ == "__main__"):
    main()