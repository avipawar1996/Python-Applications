# Question: Write a lambda function which accepts two numbers and returns Addition

# Solution:
# ---------------------------------------------------------------------------

Addition = lambda num1, num2: num1 + num2

def main():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
    sum = Addition(num1, num2)
    print(num1, "+", num2, "=", sum)

if(__name__ == "__main__"):
    main()