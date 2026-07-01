# Question: Write a lambda function using filter() which accepts a list of strings and returns list of strtings having length greater than 5.

# Solution:
# ----------------------------------------------------------------------------------

CheckIfStrLenGreaterThanFive = lambda str : len(str)>5

def main():
    lst = ["Hello", "Welcome", "To", "Marvellous", "Infosystem" ]

    str_lst = list(filter(CheckIfStrLenGreaterThanFive, lst))
    print(str_lst)

if(__name__ == "__main__"):
    main()