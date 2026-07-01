# Question: -> Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

# Solution:

def CheckIfVowel(c):
    if(c == "a" or c == "A" or 
       c == "e" or c == "E" or
       c == "i" or c == "I" or
       c == "o" or c == "O" or
       c == "u" or c == "U"
       ):
        return True
    else: return False


def main():
    char = input("Enter the character: ")
    isVowel = CheckIfVowel(char)
    if(isVowel):
        print(char, "is Vowel.")
    else:
        print(char, "is Consonant.")

if(__name__ == "__main__"):
    main()