# Write a program that accepts one number and check whether it is prime or not.
# Input: 11
# Output: Prime Number

def main():
    num = int(input("Enter the number: "))
    isPrime = CheckPrime(num)
    if(isPrime):
        print(str(num), "is prime number.")
    else:
        print(str(num), "is NOT prime number.")


def CheckPrime(num):
    for r in range(2, int(num/2) + 1):
        if(num % r == 0):
            return False
    return True

if(__name__ == "__main__"):
    main()