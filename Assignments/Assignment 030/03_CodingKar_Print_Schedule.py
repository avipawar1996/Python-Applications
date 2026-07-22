"""
Write a program that schedules a function to print:

Coding Kar...!
every 30 minutes
"""

import schedule
import time

displayMessage = lambda msg : print(msg)

def main():
    schedule.every(30).minutes.do(displayMessage, "Coding Kar...!")

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()