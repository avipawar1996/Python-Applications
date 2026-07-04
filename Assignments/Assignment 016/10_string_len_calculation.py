# Question: Write a program which accept a name from user and display the length of its name.
# Input: Marvellous         Output: 10

# Solution:
# --------------------------------------------------------------------------------

GetStrLen = lambda inpStr : len(inpStr)

# def GetStrLen(inpStr):
#     return len(inpStr)
# -------------------------------------------

# def GetStrLen(inpStr):
#     len = 0
#     for i in inpStr:
#         len = len + 1
#     return len



def main():
    inpStr = input("Enter the name: ")
    inpStrLen = GetStrLen(inpStr)

    print("Length of given name: ", inpStrLen)

if(__name__ == "__main__"):
    main()