'''
Write a program which accepts two file name from the user.
    First file is an existing file
    Second file is new file

Copy all contents from first file into the second file

Input: ABC.txt Demo.txt

Expected output:
Content of ABC.txt copied into Demo.txt
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
        print(f"Unable to read {existingFileName}: File not found")

if(__name__ == "__main__"):
    main()