"""
Write a program that deletes all empty files from specified file every hour.

The program should:
    Scan the directory recursively
    Detect the files where size is zero
    Delete all empty files
    Store deleted file path in log file
    Handle the permission error

Test the program only on sample directory.
"""

import sys, os, time, schedule, datetime,pathlib, shutil

def WriteInFile(fileName, text):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, "a")
    fobj.write(text)
    fobj.close()

def DeleteEmptyFile(src):
    border = "-" * 80
    logText = border 

    fileDeleted = list()
    fileDeleteFailed = list()
    for dirName, subDirNames, fileNames in os.walk(src):
        for fileName in fileNames:
            srcAbsPath = os.path.abspath(pathlib.Path(os.path.join(dirName, fileName)))
            if(os.path.getsize(srcAbsPath) == 0):
                try:
                    os.remove(srcAbsPath)
                    fileDeleted.append(srcAbsPath)
                except PermissionError as pe:
                    fileDeleteFailed.append(srcAbsPath)
        
    deletedFiletext = " Files Deleted: \n"
    failedFileText = ""

    if(len(fileDeleted)>0):
        for fileName in fileDeleted:
            deletedFiletext = " " + deletedFiletext + fileName + "\n"
    else:
        deletedFiletext = deletedFiletext + " No files deleted, size not 0 Byte \n"

    if(len(fileDeleteFailed)>0):
        for fileName in fileDeleteFailed:
            failedFileText = failedFileText + " File deletion failed: Permission Error: \n"
            failedFileText =  failedFileText + " " + fileName + "\n"
    
    logText = border + "\n" + deletedFiletext + failedFileText + border + "\n"

    print(logText)

    WriteInFile("Logs/FileDeleteLog.txt", logText)
    print("Delete Action Completed..")


def main():
    border = "-"*70
    print(border)
    print("Marvellous Infosystem Directory Cleanup Script")
    print(border)

    if(len(sys.argv) > 1):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <sourcedir> <destination dir>'")
            print("To know the usage, please run 'python <scriptname.py> --u'")

            ExitBorderPrint()
            return

        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script delete the empty files present in given source directory every hour")

            ExitBorderPrint()
            return

        if(len(sys.argv) == 2):
            srcDir = sys.argv[1]

            if(not os.path.exists(srcDir)):
                print("Directory not exist: ", srcDir)
                ExitBorderPrint()
                return
            
            schedule.every(1).hours.do(lambda : DeleteEmptyFile(srcDir))
            while True:
                try:
                    schedule.run_pending()
                    time.sleep(1)
                except KeyboardInterrupt:
                    ExitBorderPrint()
                    return
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.")
        ExitBorderPrint()

def ExitBorderPrint():
    border = "-"*70
    print(border)
    print("Thank You for using Marvellous Infosystem Directory Cleanup Script.")
    print(border)

if(__name__ == "__main__"):
    main()