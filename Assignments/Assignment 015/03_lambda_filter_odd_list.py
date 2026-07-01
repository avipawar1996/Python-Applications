# Question: Write a lambda function using filter() which accepts a list of numbers and returns a list of odd number

# Solution:
# ----------------------------------------------------------------------------------

CheckIfOdd = lambda num : num % 2 != 0

def main():
    lst = [11, 21, 31, 41, 51, 12, 22, 32, 42, 52]

    odd_lst = list(filter(CheckIfOdd, lst))
    print(odd_lst)

if(__name__ == "__main__"):
    main()