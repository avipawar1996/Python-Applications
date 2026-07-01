# Question: -> Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

# Solution:

def CheckIfPalindrome(num):
    reversed_num = str()
    for r in range(len(num)):
        reversed_num = reversed_num + num[len(num)-r-1]
    return reversed_num == num


def main():
    num = input("Enter the number: ")
    isPalindrome = CheckIfPalindrome(num)
    if(isPalindrome):
        print(num, "is Palindrome.")
    else:
        print(num, "is NOT Palindrome.")

if(__name__ == "__main__"):
    main()