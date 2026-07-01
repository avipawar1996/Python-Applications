# Question: Write a lambda function which accepts one number and returns the square of that number.

# Solution:
# ------------------------------------------------------

CalcSquare = lambda num : num * num

def main():
    num = int(input("Enter the number: "))
    square_of_num = CalcSquare(num)

    print("Square of", num, ": ", square_of_num)

if(__name__ == "__main__"):
    main()