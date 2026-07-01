# Question: -> Write a program which accepts radius of circle and prints radius of circle.

# Solution:

def AreaOfCircle(radius): return 3.14 * (radius * radius)

def main():
    radius = int(input("Enter the radius in cm: "))

    area_of_given_rect = AreaOfCircle(radius)
    print("Area of given circle is: ", area_of_given_rect, "sq mtr")

if(__name__ == "__main__"):
    main()