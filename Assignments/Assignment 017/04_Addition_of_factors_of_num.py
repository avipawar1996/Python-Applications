'''
Question: Write a program which accept one number and returns addition of its factors

Input: 12        16 (1+2+3+4+6)
'''

# Solution :-> ------------------------------------------------------------

def CalcFactorial(num):
    if num == 1: return 1
    elif (num>1):
        factors = num + 1
        limit = int(num/2) + 1
        for i in range(2, limit):
            if(num%i == 0):
                factors = factors + i
        return factors
    else:
        num = num*(-1)
        factors = num + 1
        limit = int(num/2) + 1
        for i in range(2, limit):
            if(num%i == 0):
                factors = factors + i
        return factors

def main():
    num = int(input("Enter the number: "))
    fact_sum = CalcFactorial(num)
    print(f"Addition of factors of {num} : {fact_sum}")

if(__name__ == "__main__"):
    main()