'''
Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, username. After creating the log file send that log file to the specified mail.

Usage: Proc_Info_All_Proc_Log.py Demo marvellousinfosystem@gmail.com

Demo is the name of Directory.
marvellousinfosystem@gmail.com is the mail Id.
'''

import psutil
import sys, os
import datetime
from zoneinfo import ZoneInfo
from File_Operations import WriteInFile
from Email_Service import validate_email, send_email

def show_greeting_init():
    return """======================================================================================
============================= Process Information Script =============================
======================================================================================

Script is started successfuly."""

def show_greeting_end():
    return """Script execution completed.
    
======================================================================================
======================================================================================"""

def show_help():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Help:
This script accepts two arguments:
1. Directory name : where the log file will be created
2. Email ID       : recipient to whom the log file will be sent

The log file contains details of all running processes:
- Process Name
- Process ID (PID)
- Username

Syntax:
    python Proc_Info_All_Proc_Log_Email.py <directory_name> <email_id>

Examples:
    python Proc_Info_All_Proc_Log_Email.py Demo marvellousinfosystem@gmail.com
        - Creates 'Demo/Process_Log.txt' and emails it to marvellousinfosystem@gmail.com

Notes:
    - You must provide both a directory name and a valid email ID.
    - Use --u for usage summary.
    - Use --h for detailed help.

======================================================================================
"""

def show_usage():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Usage: python Proc_Info_All_Proc_Log_Email.py <directory_name> <email_id>

Description:
    Creates a log file in the specified directory.
    The log file contains information about all running processes:
    - Process Name
    - Process ID (PID)
    - Username
    After creation, the log file is sent to the given email address.

Example:
    python Proc_Info_All_Proc_Log_Email.py Demo marvellousinfosystem@gmail.com

======================================================================================
"""

def show_invalid():
    return """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Error: Invalid or insufficient arguments.

Correct syntax:
    python Proc_Info_All_Proc_Log_Email.py <directory_name> <email_id>

To see usage information, run:
    python Proc_Info_All_Proc_Log_Email.py --u
    or
    python Proc_Info_All_Proc_Log_Email.py --usage

To see detailed help, run:
    python Proc_Info_All_Proc_Log_Email.py --h
    or
    python Proc_Info_All_Proc_Log_Email.py --help

Example:
    python Proc_Info_All_Proc_Log_Email.py Demo avi1996pawar@gmail.com

======================================================================================
"""

def get_log_header():
    return """
======================================================================================
============================= Process Information Script =============================
======================================================================================
"""

def get_log_footer():
    return """
======================================================================================
======================================================================================
"""

get_process_details = lambda : psutil.process_iter()

def log_process_details(dir_name, rec_email):
    file_stamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    mail_stamp = datetime.datetime.now().strftime("%d/%m/%Y_%I:%M:%S %p")
    file_name = os.path.join(dir_name, f"Proc_{file_stamp}.log")
    tz=ZoneInfo("Asia/Kolkata")

    WriteInFile(file_name, get_log_header(), "a")

    proc_list = get_process_details()

    for proc in proc_list:
        log_text = ""
        try: 
            log_text = f"""
--------------------------------------------------------------------------------------
Process ID        : {proc.pid}
Process Name      : {proc.name()}
Process Status    : {proc.status()}
Process Started   : {datetime.datetime.fromtimestamp(proc.create_time(), tz=tz)}
--------------------------------------------------------------------------------------

"""
        except Exception as e: 
            log_text = f"""
--------------------------------------------------------------------------------------
Process ID        : f{e} 
--------------------------------------------------------------------------------------

"""

        WriteInFile(file_name=file_name, file_content=log_text, mode="a")

    WriteInFile(file_name, get_log_footer(), "a")
    if(validate_email(rec_email)):
        print("\nEmail is valid, trying to send email.")
        app_email = os.environ.get("app_email")
        app_password = os.environ.get("app_password")
        rec_email = rec_email
        subject = f"Process Monitoring - {mail_stamp}"

        body= """
Jay Ganesh !

Process Monitoring is completed. Please find attached log file for more details on running processes.

Thank You.
Avinash P.
"""
        attachments = [rf"{os.path.abspath(file_name)}"]
        email_status = send_email(sender_email=app_email, password=app_password, rec_email=rec_email, subject=subject, body=body, attachments=attachments)
        if(email_status): print("Email sent successfully.")
        else: print("Email sending failed.")
    return

def main():
    options = sys.argv
    if(len(options) == 2 and (options[1] == "--h" or options[1] == "--help")):
        print(show_help())
    elif(len(options) == 2 and (options[1] == "--u" or options[1] == "--usage")):
        print(show_usage())
    elif(len(options) == 3):
        print(show_greeting_init())
        dir_path = options[1]
        email = options[2]
        log_process_details(dir_path, email)
        print(show_greeting_end())
    else:
        print(show_invalid())

if(__name__ == "__main__"):
    main()