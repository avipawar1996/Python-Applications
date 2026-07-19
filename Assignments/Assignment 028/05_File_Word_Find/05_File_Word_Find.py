'''
Write a program which accepts a file name and word from the user and checks whether that word is present in the file or not.

Input: Demo.txt Marvellous

Expected output:
Display whether the Marvellous is found in Demo.txt or not
'''

import sys, os

def ChkIfFileContains(fileName:str, searchTerm:str):
    fobj = open(fileName)
    lines = fobj.readlines()
    for line in lines:
        if line.__contains__(searchTerm):
            return True
        
    fobj.close()
    return False


def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    fileName, searchTerm  = sys.argv[1], sys.argv[2]

    if ChkFileExists(fileName):
        isSearchTermFound = ChkIfFileContains(fileName=fileName, searchTerm=searchTerm)
        if isSearchTermFound:
            print(f"Search Term '{searchTerm}' is present in '{fileName}'")
        else:
            print(f"No match found for: '{searchTerm}' in File: '{fileName}")
    else:
        print(f"Unable to search: File not found")

if(__name__ == "__main__"):
    main()