# Question: Write a program which accepts one number from user and print that number of "*" on screen

# Input: 5          Output: *   *   *   *   *

# Solution: 
# ---------------------------------------------------------------------------------------

printMsg = lambda msg, end="\n" : print(msg, end=end)
# def printMsg(msg, end):
#     print(msg, end=end)

def main():
    num = int(input("Enter the number: "))
    for i in range(num):
        printMsg("*", "    ")

if(__name__ == "__main__"):
    main()