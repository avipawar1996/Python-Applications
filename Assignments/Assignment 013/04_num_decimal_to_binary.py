# Question: -> Write a program which accepts one prints binary of it.

# Solution:
# ----------------------------------------------------------------------------

# def ConvertToBase2(num): return bin(num)

def ConvertToBase2(num):
    temp = num
    bin_val = 0
    place = 1

    while(temp != 0):
        bin_val_temp = temp % 2 
        temp = int(temp / 2)
        bin_val = bin_val + (place * bin_val_temp)
        place = place * 10
    return bin_val

def main():
    num = int(input("Enter the number: "))

    dec_to_bin = ConvertToBase2(num)
    print("Binary of", num, ":", dec_to_bin)

if(__name__ == "__main__"):
    main()