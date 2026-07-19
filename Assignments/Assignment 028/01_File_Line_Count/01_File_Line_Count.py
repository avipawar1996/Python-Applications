'''
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input: Demo.txt

Expected output:
Total number of lines in Demo.txt: 
'''

import sys, os

def CountLines(fileName):
    fobj = open(fileName)
    lineCount = len(fobj.readlines())

    fobj.close()
    
    return lineCount

def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName = sys.argv[1]

    if ChkFileExists(fileName):
        lineCount = CountLines(fileName)
        print(f"Number of lines in '{fileName}': {lineCount}")
    else:
        print(f"Unable to read '{fileName}': File not found")

if(__name__ == "__main__"):
    main()