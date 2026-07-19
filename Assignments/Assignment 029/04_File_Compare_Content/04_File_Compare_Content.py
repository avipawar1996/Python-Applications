'''
Write a program which accepts two file names through command line arguments and compares the content of both files.

    If both files contains the same content, display Success
    Otherwise display Failure

Input: (command line):
Demo.txt Hello.txt

Expected output:
Success or Failure
'''

import sys, os

def ReadFileContent(fileName:str):
    fobj = open(fileName)
    fileContent = fobj.read()

    fobj.close()
    return fileContent


def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    file1Name, file2Name  = sys.argv[1], sys.argv[2]

    for file in [file1Name, file2Name]:
        if (not ChkFileExists(file)):
            print(f"Content reading failed: File {file} not found")
            return

    if(ReadFileContent(file1Name) == ReadFileContent(file2Name)):
        print("Success")
    else:
        print("Failure")

if(__name__ == "__main__"):
    main()