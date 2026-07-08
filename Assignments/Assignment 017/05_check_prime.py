'''
Question: Write a program which accept one number from user and check whether the number is prime or not
Input: 5            Output: Prime Number
'''

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True
        
def main():
    num = int(input("Enter the number: "))
    isPrime = checkPrime(num)
    if(isPrime == True):
        print(f"{num} is Prime Number") 
    else:
        print(f"{num} is Not Prime Number")

if __name__ == "__main__":
    main()