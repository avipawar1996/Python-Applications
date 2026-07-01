# Question: -> Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5  4  3  2  1

# Solution:

def GetNumbersUptoN(num):
    n_numbers = list()
    for i in range(1, num + 1):
        n_numbers.append(num - (i - 1))
    return n_numbers


def main():
    num = int(input("Enter the number: "))
    n_numbers = GetNumbersUptoN(num)
    print("Numbers from", num, "to 1", end=" :  ")
    for i in n_numbers:
        print(i, end="    ")

if(__name__ == "__main__"):
    main()