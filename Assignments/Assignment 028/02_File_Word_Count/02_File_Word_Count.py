'''
Write a program which accepts a file name from the user and counts the total number of words present in the file.

Input: Demo.txt

Expected output:
Total number of words in Demo.txt: 
'''

import sys, os

def CountWords(fileName):
    fobj = open(fileName)
    lines = fobj.readlines()
    wordCount = 0
    for line in lines:
        wordCount = wordCount + len(line.split())

    fobj.close()
    
    return wordCount


def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName = sys.argv[1]

    if ChkFileExists(fileName):
        wordCount = CountWords(fileName)
        print(f"Number of words in '{fileName}': {wordCount}")
    else:
        print(f"Unable to read number of words in {fileName}: File not found")

if(__name__ == "__main__"):
    main()