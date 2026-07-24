"""
Create a function named:
DisplayMessage(msg)

Schedule the function using:

schedule.every(5).seconds.do(DisplayMessage, message)

This message should be accepted from user.

"""

import sys, time, schedule

DisplayMessage = lambda msg: print(msg)

def main():
    border = "-"*70
    print(border)
    print("Marvellous Infosystem Script")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <message to display>'")

            print("To know the usage, please run 'python <scriptname.py> --h'")
        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script prints given text message every 5 seconds.")
        else:
            msg = sys.argv[1]

            schedule.every(5).seconds.do(DisplayMessage, msg)

            while True:
                try:
                    schedule.run_pending()
                    time.sleep(1)
                except KeyboardInterrupt:
                    ExitBorderPrint()
                    return
            
                
    else:
        print("Invalid Arguments. Please use '<scriptfile>.py --h or --u' for more information.")   
  
def ExitBorderPrint():
    border = "-"*70
    print(border)
    print("Thank You for using Marvellous Infosystem Script.")
    print(border)

if(__name__ == "__main__"):
    main()