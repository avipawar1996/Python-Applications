'''
Write a program which accepts a file name from the user and display the content of file line by line on the screen

Input: Demo.txt

Expected output:
Display each line of Demo.txt one by one
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