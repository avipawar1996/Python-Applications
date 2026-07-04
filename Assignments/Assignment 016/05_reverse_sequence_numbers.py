# Question: Write a program which display 10 to 1 on screen.
# Output: 10    9   8   7   6   5   4   3   2   1

# Solution:->
# --------------------------------------------------------------------------------

def DisplayMsg(msg): print(msg)
# DisplayMsg = lambda msg : print(msg)

def main():
    n = int(input("Enter the reverse number sequence print starting: "))
    for i in range(n): DisplayMsg(n-i)

if(__name__ == "__main__"):
    main()