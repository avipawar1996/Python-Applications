'''
Write a program which accepts a file name from the user and display the entire content on the console.

Input: Demo.txt

Expected output:
Display each line of Demo.txt on console
'''

import sys, os

def ReadFileContent(fileName):
    fobj = open(fileName)
    fileContent = fobj.read()

    fobj.close()
    
    return fileContent

def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName = sys.argv[1]

    if ChkFileExists(fileName):
        fileContent  = ReadFileContent(fileName)
        print(f"File '{fileName}' content: \n{fileContent}")
    else:
        print(f"Unable to read '{fileName}': File not found")

if(__name__ == "__main__"):
    main()