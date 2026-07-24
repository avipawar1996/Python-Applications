"""
Write a program that scans a specified directory every time.

The task should display:

    Directory Name
    Number of files
    Number of sub-directorie
    Date and time of scanning

Use os module.

Example output:
# Directory scanned: D:/Python/Git/Assignments
Total Files: 15
Total SubDirectories: 4
Scan time: 25-07-2026 04:30:00 PM

"""

import sys, time, schedule, os, pathlib, datetime

def DirScanner(dirPath):
    dirLen, totalSubDirs, totalFiles = 0, 0, 0
    print("inside dirscanner")
    for dirNames, subDirNames, fileNames in os.walk(dirPath):
        totalSubDirs += len(subDirNames)
        totalFiles += len(fileNames)

    print("Directory Scanned: ", dirPath)
    print("Total Files: ", totalFiles)
    print("Total SubDirectories: ", totalSubDirs)
    print("Scan time:", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    border = "-"*70
    print(border)
    print("Directory Scanning Script")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <directory path>'")

            print("To know the usage, please run 'python <scriptname.py> --h'")
        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script scans specified directory every minute periodically.")
        else:

            dirPath = pathlib.Path(sys.argv[1]).expanduser().resolve()
            DirScanner(dirPath=dirPath)
            schedule.every(1).minutes.do(DirScanner, dirPath)

            while True:
                try:
                    schedule.run_pending()
                    time.sleep(1)
                except KeyboardInterrupt:
                    ExitBorderPrint()
                    return
            
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.")   

def ExitBorderPrint():
    border = "-"*70
    print(border)
    print("Thank You for using Directory Scanning Script.")
    print(border)

if(__name__ == "__main__"):
    main()