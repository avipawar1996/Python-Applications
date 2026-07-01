# Question:-> Write a program that accepts one number and prints all even numbers till that number.
# Input: 10
# Output:  2   4   6   8   10

def FindNEvenNumbers(num):
    n_even_numbers = list()
    for i in range(1, num+1):
        if(i % 2 == 0):
            n_even_numbers.append(i)
    return n_even_numbers

def main():
    num = int(input("Enter the number: "))
    n_even_numbers = FindNEvenNumbers(num)

    for num in n_even_numbers:
        print(num, end="    ")
        
if(__name__ == "__main__"):
    main()