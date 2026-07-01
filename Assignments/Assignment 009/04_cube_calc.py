# Question:-> Write a program that accepts one number and prints square of that number.
# Input: 5
# Output: 125

# Solution:->

def main():
    num = int(input("Enter the number: "))
    cube_of_num = CalcCube(num)

    print("Cube of", num, "is:", cube_of_num)

def CalcCube(num):
    return num * num * num

if(__name__ == "__main__"):
    main()