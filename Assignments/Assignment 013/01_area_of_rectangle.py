# Question: -> Write a program which accepts length and width of rectangle and prints area.

# Solution:

def AreaOfRectangle(length, width): return length * width


def main():
    length = int(input("Enter the length in cm: "))
    width = int(input("Enter the width in cm: "))

    area_of_given_rect = AreaOfRectangle(length, width)
    print("Area of given rectangle is: ", area_of_given_rect, "sq mtr")



if(__name__ == "__main__"):
    main()