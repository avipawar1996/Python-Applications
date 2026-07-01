# Question: -> Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

# Solution:

def ReverseNumber(num):
    reversed_num = str()
    for r in range(len(num)):
        reversed_num = reversed_num + num[len(num)-r-1]
    return reversed_num


def main():
    num = input("Enter the number: ")
    reversed_num = ReverseNumber(num)
    print("Reverse of", num, "is:", reversed_num)

if(__name__ == "__main__"):
    main()