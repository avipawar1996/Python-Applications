# Question 6:
# Write a program to display:
# Data Type
# Memory Address
# Size in Bytes of a variable entered by user

# Solution:
from sys import getsizeof

def main():

    # As per need the data type can be converted if appropriate input is given eg. int, float etc
    user_input = input("Enter the value: ")

    # to print the type
    print("Type is: ", type(user_input))

    # to print the Memory Address
    print("Memory Address of", user_input, "is: ", id(user_input))

    # to print the type
    print("Size of", user_input, "is: ",  getsizeof(user_input), "Bytes")

if(__name__ == "__main__"):
    main()
