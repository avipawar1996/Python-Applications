'''
Question: Write a program which contain lambda function which accept two numbers and return their multiplication

Input: 4    3        Output: 12
Input: 6    3        Output: 18

'''

CalcMul = lambda num1, num2 : num1 * num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    mul = CalcMul(num1, num2)
    print(f"{num1} * {num2} = {mul}")

if __name__ == "__main__":
    main()