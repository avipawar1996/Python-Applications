# Question:-> Write a program that accepts one number and prints multiplication table of that number.
# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40

def TableMultiplication(num):
    mul_table = list()

    for i in range(10):
        mul_table.append((i+1) * num)
    return mul_table

def main():
    num = int(input("Enter the number: "))
    table_of_num = TableMultiplication(num)

    for t in table_of_num:
        print(t, end="    ")

if(__name__ == "__main__"):
    main()