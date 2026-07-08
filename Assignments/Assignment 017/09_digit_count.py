'''
Write a program which accept number from user and returns the number of digit in it.

Input: 5187934            Output: 37
'''

DigCount = lambda num: len(num)

# def DigCount(num):
#     count = 0
#     for i in num:
#         count = count + 1
#     return count

def main():
    num = input("Enter the number to count digit for: ")
    dig_count = DigCount(num)
    print(f"Digits count in the number {num} is: {dig_count}")

if __name__ == "__main__":
    main()