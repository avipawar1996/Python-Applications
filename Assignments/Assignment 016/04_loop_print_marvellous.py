# Question: Write a program which display 5 times Marvellous on screen.
# Output: 
# Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

# Solution:->
# --------------------------------------------------------------------------------

def DisplayMsg(msg):
    print(msg)

# DisplayMsg = lambda msg : print(msg)

def main():
    msg = "Marvellous" 
    # msg = input("Enter the message to be printed? ")

    n = int(input("How many times message to be printed? "))

    for i in range(n):
        DisplayMsg(msg)

if(__name__ == "__main__"):
    main()