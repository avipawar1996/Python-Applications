# Question: -> Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

# Solution:

def FindFactors(num):
    factors_of_num = list()
    for i in range(1, num+1):
        if(int(num) % i == 0):
            factors_of_num.append(i)

    return factors_of_num

def main():
    num = int(input("Enter the character: "))
    factors_of_num = FindFactors(num)
    
    print("Factors of", num, ":", end=" ")
    for factor in factors_of_num:
        print(factor, end="    ")

if(__name__ == "__main__"):
    main()