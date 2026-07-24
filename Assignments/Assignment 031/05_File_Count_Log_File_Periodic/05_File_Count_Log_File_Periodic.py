"""
Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes

Write the result into:

DirectoryCountLog.txt
Each entry should contain:

    Directory Path
    Number of Files
    Date and Time
"""

import sys, time, schedule, os, pathlib, datetime

def WriteInFile(fileName, text, mode="r"):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, mode=mode)
    fobj.write(text)
    fobj.close()

def LogFileCountInDir(dirPath):
    fileCount = 0
    timeStamp = getTimeStamp()
    fullPath = pathlib.Path(dirPath).resolve()

    print(fullPath)

    for dirName, subDirNames, fileNames in os.walk(dirPath):
        fileCount = fileCount + len(fileNames)
    logText = f'''
    ------------------------------------------------------
    Directory Path: {fullPath}
    Number of Files: {fileCount}
    Date and Time: {timeStamp}
    ------------------------------------------------------
    '''
    WriteInFile("Logs/DirectoryCountLog.txt",logText, "a")

getTimeStampForFileName = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
getTimeStamp = lambda : datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
getLogText = lambda: f"Log file created successfully.\nCreation Time: {getTimeStamp()}"
getLogFileName = lambda : "DirectoryCountLog.txt"

def main():
    border = "-"*70
    print(border)
    print("Log File Creation Script")
    print(border)

    if (len(sys.argv) == 2):

        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <directory path>'")
            print("To know the usage, please run 'python <scriptname.py> --h'")

        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script creates log file every 10 minute periodically.")

        else:
            dirPath = sys.argv[1]
            if(not os.path.exists(dirPath)):
                print(f"Given path does not exist: {dirPath}")
                ExitScript()
    
            else:
                schedule.every(3).seconds.do(lambda: LogFileCountInDir(dirPath=dirPath))

                while True:
                    try:
                        schedule.run_pending()
                        time.sleep(1)
                    except KeyboardInterrupt:
                        ExitScript()
                        return
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.")   
        ExitScript()

def ExitScript():
    border = "-"*70
    print(border)
    print("Thank You for using Log File Creation Script.")
    print(border)

if(__name__ == "__main__"):
    main()