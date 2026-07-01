# Question:-> Write a program that accepts one number and prints all odd numbers till that number.
# Input: 10
# Output:  1   3   5   7   9

def FindNOddNumbers(num):
    n_odd_numbers = list()
    for i in range(1, num+1):
        if(i % 2 == 1):
            n_odd_numbers.append(i)
    return n_odd_numbers

def main():
    num = int(input("Enter the number: "))
    n_odd_numbers = FindNOddNumbers(num)

    for num in n_odd_numbers:
        print(num, end="    ")
        
if(__name__ == "__main__"):
    main()