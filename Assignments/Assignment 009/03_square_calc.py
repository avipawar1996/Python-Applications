# Question:-> Write a program that accepts one number and prints square of that number.
# Input: 5
# Output: 25

# Solution:->

def main():
    num = int(input("Enter the number: "))
    square_of_num = CalcSquare(num)

    print("Square of", num, "is:", square_of_num)

def CalcSquare(num):
    return num * num

if(__name__ == "__main__"):
    main()