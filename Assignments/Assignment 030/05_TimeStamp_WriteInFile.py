"""
Write a program that executes every 5 minutes.
Task should write the current date and time into file named:
marvellous.txt

New entries should be appended without removing previous entries.

Example file contents:
Task executed at: 25-07-2026 04:30:00 PM
Task executed at: 25-07-2026 04:35:00 PM
Task executed at: 25-07-2026 04:40:00 PM

"""

import schedule
import time, datetime

def WriteInFile(fileName:str, text:str):
    fobj = open(fileName, "a")
    fobj.write(text+"\n")
    fobj.close()

getCustomDateTimeFormat = lambda : datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def main():

    schedule.every(5).minutes.do(lambda : WriteInFile("marvellous.txt", f"Task executed at: {getCustomDateTimeFormat()}"))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()