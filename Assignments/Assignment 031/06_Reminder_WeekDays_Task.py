"""
Write a program that schedules the following messages:

    Monday at 9:00AM: Start your weekly goals
    Wednesday ar 5:00PM: Review your weekly progress
    Friday at 6:00PM: Weekly work completed

Use:
    schedule.every().monday.at(...)
    schedule.every().wednesday.at(...)
    schedule.every().friday.at(...)
"""

import sys, time, schedule, datetime

def DisplayReminderMessage(msg):
    print(msg)

def main():
    border = "-"*70
    print(border)
    print("Weekly Task Reminder")
    print(border)

    if (len(sys.argv) == 2):

        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py>'")
            print("To know the usage, please run 'python <scriptname.py> --h'")

        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script reminds the weekly scheduled tasks")

    elif(len(sys.argv) == 1):

        schedule.every().monday.at("09:00:00").do(lambda : DisplayReminderMessage("Start your weekly goals"))

        schedule.every().wednesday.at("17:00:00").do(lambda : DisplayReminderMessage("Review your weekly progress"))

        schedule.every().friday.at("18:00:00").do(lambda : DisplayReminderMessage("Weekly work completed"))

        while True:
            try:
                schedule.run_pending()
                time.sleep(1)

            except KeyboardInterrupt:
                ExitBorder()
                return
        
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.") 
        ExitBorder() 
  
def ExitBorder():
    border = "-"*70
    print(border)
    print("Thank You for using Weekly Task Reminder.")
    print(border)

if(__name__ == "__main__"):
    main()