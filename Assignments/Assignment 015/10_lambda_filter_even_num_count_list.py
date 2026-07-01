# Question: Write a lambda function using filter() which accepts a list of numbers and returns a count of even numbers

# Solution:
# ----------------------------------------------------------------------------------

CheckIfEven = lambda num,  : num % 2 == 0

def main():
    lst = [12, 15, 19, 26, 70, 45, 90, 100]

    even_lst = len(list(filter(CheckIfEven, lst)))
    even_count = even_lst
    print(even_count)

if(__name__ == "__main__"):
    main()