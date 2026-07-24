"""
Write a program that monitors the size of a specified file every 30 seconds.

Write the following details into:
    FileSizeLog.txt
            File Path
            File Size in Bytes
            Date and Time

Handle the situation where the file does not exist.
"""

import sys, os, time, schedule, datetime,pathlib

getTimeStamp = lambda : datetime.datetime.strftime("%d_%m_%Y_%H_%M_%S")

def WriteInFile(fileName, text, mode="r"):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, mode=mode)
    fobj.write(text)
    fobj.close()

getTimeStampForFileName = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
getFileName = lambda : f"Logs/FileSizeLog.txt"
getLogText = lambda srcFileFullPath: f"""
-------------------------------------------------------------------------
    FilePath: {srcFileFullPath}
    Monitoring Date & Time: {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}
    File Size ib Bytes: {os.path.getsize(srcFileFullPath)}
-------------------------------------------------------------------------
"""

def CreateFileScripting(srcFileFullPath):
    logFileName = getFileName()
    text = getLogText(srcFileFullPath)
    WriteInFile(logFileName, text=text, mode="a")

def main():
    border = "-"*70
    print(border)
    print("Marvellous Infosystem File Creation Script")
    print(border)

    if(len(sys.argv) == 2):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <message to display> <interval in sec>'")
            print("To know the usage, please run 'python <scriptname.py> --u'")

        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("""
            This script Create the file every minute as below example-

            Example:
                fileName: File_24_07_2026_14_09_07.txt
                Creation Date: 2026-07-24
                Creation Time: 02:09:07 PM
            """)

        else :

            fileFullPath = pathlib.Path(sys.argv[1]).expanduser().resolve()
            if(not os.path.exists(fileFullPath)):
                print("File does not exist: ", sys.argv[1])
                ExitBorderPrint()
                return
            
            schedule.every(2).seconds.do(lambda : CreateFileScripting(fileFullPath))
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
    print("Thank You for using Marvellous Infosystem File Creation Script.")
    print(border)

if(__name__ == "__main__"):
    main()