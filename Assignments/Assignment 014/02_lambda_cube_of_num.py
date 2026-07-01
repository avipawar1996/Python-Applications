# Question: Write a lambda function which accepts one number and returns the cube of that number.

# Solution:
# ------------------------------------------------------

CalcCube = lambda num : num * num * num

def main():
    num = int(input("Enter the number: "))
    cube_of_num = CalcCube(num)

    print("Cube of", num, ": ", cube_of_num)

if(__name__ == "__main__"):
    main()