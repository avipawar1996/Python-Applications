# Question:-> Write a program that accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

# Solution:->

def main():
    num = int(input("Enter the number: "))
    isDivisible_by_3_5 = testDivisibility(num)

    if(isinstance(isDivisible_by_3_5, str)):
        print(isDivisible_by_3_5)
        
    else:
        print("Divisible by 3 and 5.")


def testDivisibility(num):
    if((num % 3 == 0) and (num % 5 == 0)):
        return True
    
    elif(num % 3 == 0 and (num % 5 != 0)):
        return "Divisible by 3 only."
    
    else:
        return "Divisible by 5 only."

if(__name__ == "__main__"):
    main()