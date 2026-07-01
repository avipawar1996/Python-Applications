# Question: -> Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

# Solution:

def GetNumbersUptoN(num):
    n_numbers = list()
    for i in range(1, num + 1):
        n_numbers.append(i)
    return n_numbers


def main():
    num = int(input("Enter the number: "))
    n_numbers = GetNumbersUptoN(num)
    print("Numbers from 1 to", num, end=" : ")
    for i in n_numbers:
        print(i, end="    ")

if(__name__ == "__main__"):
    main()