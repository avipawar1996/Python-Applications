"""
Write a program that executes every day at 09:00 AM and prints:
Namaskar...

use:
schedule.every().day.at("09:00").do(...)
"""

import schedule
import time, datetime

displayMessage = lambda msg : print(msg, f"{datetime.datetime.now()}")

def main():
    schedule.every().day.at("09:00:00").do(lambda : displayMessage("Namaskar..."))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()