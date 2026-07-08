'''
Write a program which accept number from user and returns the number of digit in it.

Input: 5187934            Output: 37
'''

def DigCount(num):
    sum = 0
    for dig in num:
        sum = sum + int(dig)
    return sum

def main():
    num = input("Enter the number to count digit for: ")
    dig_sum = DigCount(num)
    print(f"Sum of digits of {num} is: {dig_sum}")

if __name__ == "__main__":
    main()