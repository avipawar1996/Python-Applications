"""
Write a program that displays the current date and time after every one minute.

Use the datetime module.

Expected Output:
Current date and Time: 25-07-2026 04:30:00 PM
"""

import schedule
import time, datetime

displayMessage = lambda msg : print(msg)
getCustomDateTimeFormat = lambda : f'Current Date and Time is:  {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}'

def main():
    schedule.every(1).minutes.do(lambda : displayMessage(getCustomDateTimeFormat()))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()