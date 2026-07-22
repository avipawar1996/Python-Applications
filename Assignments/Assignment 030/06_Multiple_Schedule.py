"""
Write a script that schedules the following tasks:

Print Lunch Time! everyday at 01.00 PM.
print Wrap up work everyday at 06:00 PM.

Both tasks should be handled by separate functions.
"""

import schedule
import time

LunchTime = lambda : print("Lunch Time")
WrapUpForTheDay = lambda : print("Wrap up work")

def main():

    schedule.every().day.at("13:00:00").do(LunchTime)
    schedule.every().day.at("18:00:00").do(WrapUpForTheDay)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()