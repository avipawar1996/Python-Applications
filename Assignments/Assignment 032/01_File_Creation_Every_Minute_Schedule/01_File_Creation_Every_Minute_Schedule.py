"""
Write a program that creates a new text file every minute.

The file name should contain current timestamp.

Example:
File_25_07_2026_16_30_00.txt

Write the following information into the file:
    Filename:
    Creation Date:
    Creation Time:
"""

import sys, os, time, schedule, datetime,pathlib

getTimeStamp = lambda : datetime.datetime.strftime("%d_%m_%Y_%H_%M_%S")

def WriteInFile(fileName, text):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, "w")
    fobj.write(text)
    fobj.close()

getTimeStampForFileName = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
getFileName = lambda : f"File_{getTimeStampForFileName()}.txt"
getLogText = lambda fileName: f"""
-------------------------------------------------------------------------
    fileName: {fileName}
    Creation Date: {datetime.datetime.now().date()}
    Creation Time: {datetime.datetime.now().strftime("%I:%M:%S %p")}
-------------------------------------------------------------------------
"""

def CreateFileScripting():
    fileName = getFileName()
    print(fileName)
    text = getLogText(fileName)
    filePath = os.path.join("Data", fileName)
    WriteInFile(filePath, text=text)

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

    elif (len(sys.argv) == 1) :

        schedule.every(1).minutes.do(lambda : CreateFileScripting())
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