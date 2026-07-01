# Question:-> Write a program that accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def sumOfFirstNNatNumbers(num):
    sum = 0
    for i in range(num):
        sum = sum + (i + 1)
    return sum

def main():
    num = int(input("Enter the number: "))
    sum_of_n_nat_num = sumOfFirstNNatNumbers(num)

    print("Sum of first", num, "natural numbers is: ", sum_of_n_nat_num)

if(__name__ == "__main__"):
    main()