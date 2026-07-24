"""
Write a program that creates a new log file after every ten minutes.

The filename should contain the current date and time.

Example:
MarvellousLog_25_07_2026_16_30_00.txt
The file should contain:

Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
"""

import sys, time, schedule, os, pathlib, datetime

def WriteInFile(fileName, text):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, "w")
    fobj.write(text)
    fobj.close()

getTimeStampForFileName = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
getTimeStamp = lambda : datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
getLogText = lambda: f"Log file created successfully.\nCreation Time: {getTimeStamp()}"
getLogFileName = lambda : f"Logs/Marvellous_{getTimeStampForFileName()}.txt"

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
    elif (len(sys.argv) == 1):

        schedule.every(10).minutes.do(lambda: WriteInFile(getLogFileName(), getLogText()))

        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                ExitScriptBorder()
                return
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.")   

def ExitScriptBorder():
    border = "-"*70
    print(border)
    print("Thank You for using Log File Creation Script.")
    print(border)

if(__name__ == "__main__"):
    main()