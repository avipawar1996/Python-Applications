'''
Write a program which accepts an existing file name through command line arguments, create a new file named Demo.txt, and copies all contents from the given file into Demo.txt

Input:
ABC.txt Demo.txt

Expected output:
Create Demo.txt and copy content of ABC.txt into Demo.txt
'''

import sys, os

def ReadFileContent(fileName):
    fobj = open(fileName)
    fileContent = fobj.read()

    fobj.close()

    return fileContent

def CreateFile(newFileName, existingFileContent):
    fobj = open(newFileName, "w")
    fobj.write(existingFileContent)
    fobj.close()

    return True

def ChkFileExists(fileName):
    return os.path.exists(fileName)

def main():
    existingFileName, newFileName = sys.argv[1], sys.argv[2]

    if ChkFileExists(existingFileName):

        existingFileContent  = ReadFileContent(existingFileName)
        isCreateFileSuccess = CreateFile(newFileName = newFileName, existingFileContent=existingFileContent)

        if isCreateFileSuccess:
            print(f"File '{newFileName}' created and pasted content of {existingFileName} in new file successfully")
        else:
            print(f"File {newFileName} was not created.")

    else:
        print(f"Unable to copy {existingFileName}: File not found")

if(__name__ == "__main__"):
    main()