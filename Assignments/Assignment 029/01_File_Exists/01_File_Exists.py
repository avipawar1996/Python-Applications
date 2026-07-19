'''
Write a program which accepts a file name from the user and checks whether that file exists in curret directory or not.

Input: Demo.txt

Expected output:
Display whether Demo.txt exists or not:
'''

import sys, os

def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName = sys.argv[1]

    if ChkFileExists(fileName):
        print(f"'{fileName}' is present in current directory.")
    else:
        print(f"'{fileName}' is NOT present in current directory.")


if(__name__ == "__main__"):
    main()