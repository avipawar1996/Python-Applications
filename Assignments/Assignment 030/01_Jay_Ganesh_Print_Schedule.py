"""
Write a program that prints:
Jay Ganesh...
Every 2 seconds.

Use:
schedule.every(2).seconds.do(...)

Expected Output:
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
"""

import schedule
import time

displayMessage = lambda msg : print(msg)

def main():
    schedule.every(2).seconds.do(displayMessage, "Jay Ganesh...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()