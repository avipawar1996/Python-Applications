# Question:-> Write a program that accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def factorialCalc(num):
    fact = 1
    for i in range(num):
        fact = fact * (i + 1)
    return fact

def main():
    num = int(input("Enter the number: "))
    factorial_of_num = factorialCalc(num)

    print("Factorial of", num, ": ", factorial_of_num)

if(__name__ == "__main__"):
    main()