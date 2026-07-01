# Question: Write a lambda function using map() which accepts a list of numbers and returns a list of square of each number

# Solution:
# ----------------------------------------------------------------------------------

CalcSquare = lambda num : num * num

def main():
    lst = [11, 21, 31, 41, 51]

    sq_lst = list(map(CalcSquare, lst))
    print(sq_lst)

if(__name__ == "__main__"):
    main()