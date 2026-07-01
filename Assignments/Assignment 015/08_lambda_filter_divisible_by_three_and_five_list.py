# Question: Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

# Solution:
# ----------------------------------------------------------------------------------

CheckIfDivisibleByFiveAndThree = lambda num : num % 3 == 0 and num % 5 == 0

def main():
    lst = [12, 15, 19, 26, 70, 45, 90]

    numbers_lst = list(filter(CheckIfDivisibleByFiveAndThree, lst))
    print(numbers_lst)

if(__name__ == "__main__"):
    main()