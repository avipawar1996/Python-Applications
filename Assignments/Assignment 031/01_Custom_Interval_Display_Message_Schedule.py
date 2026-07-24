"""
Write a program that accepts:
    Message from the user
    Time interval in the seconds

Schedule the program to display the message after the specified interval.

Example output:
Enter Message: Jay Ganesh
Enter the interval: 5

Example Output:
Jay Ganesh
every five seconds.

Validate that the interval is greater than zero

"""

import sys, time, schedule

DisplayMessage = lambda msg: print(msg)

def main():
    border = "-"*70
    print(border)
    print("Marvellous Infosystem Script")
    print(border)

    if (len(sys.argv) == 2 or len(sys.argv)==3):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <message to display> <interval in sec>'")

            print("To know the usage, please run 'python <scriptname.py> --u'")
        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script prints given text message after specific interval provided as by user.")
        elif(len(sys.argv) == 3):
            msg = sys.argv[1]
            try:
                interval = int(sys.argv[2])
            except ValueError as v:
                print(f"Unable to convert to time in seconds (int): {v}")
                return

            if(interval > 0):
                schedule.every(interval).seconds.do(lambda : DisplayMessage(msg=msg)) 

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
    print("Thank You for using Marvellous Infosystem Script.")
    print(border)

if(__name__ == "__main__"):
    main()