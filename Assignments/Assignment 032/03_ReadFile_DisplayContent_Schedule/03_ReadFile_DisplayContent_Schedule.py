"""
Write a program that reads and displays the content of specified text file every minute.

Handle the following conditionas:

    File does not exist
    File is empty
    Permission is denied
    File cannot be opened
"""

import sys, os, time, schedule, datetime,pathlib

getTimeStamp = lambda : datetime.datetime.strftime("%d_%m_%Y_%H_%M_%S")

getTimeStampForFileName = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
getFileName = lambda : f"Logs/FileSizeLog.txt"
getLogText = lambda srcFileFullPath: f"""
-------------------------------------------------------------------------
    FilePath: {srcFileFullPath}
    Monitoring Date & Time: {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}
    File Size ib Bytes: {os.path.getsize(srcFileFullPath)}
-------------------------------------------------------------------------
"""

def ReadDisplayFileContent(srcFileFullPath):

    if(os.path.isdir(srcFileFullPath)):
        print("Error: File cannot be read because path is directory")
        return
    if(os.path.getsize(srcFileFullPath) == 0):
        print("Source File is empty.")
        return
    try:
        fobj = open(srcFileFullPath, "r")
        filecontent = fobj.read()
        print(filecontent)
    except PermissionError:
        print("Error: Permission is denied")
    except OSError as e:
        print(f"Error:File cannot be opened. ({e})")

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
            filePath = sys.argv[1]
            if(not os.path.exists(filePath)):
                print("File does not exist: ", sys.argv[1])
                ExitBorderPrint()
                return
            
            schedule.every(2).seconds.do(lambda : ReadDisplayFileContent(filePath))
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