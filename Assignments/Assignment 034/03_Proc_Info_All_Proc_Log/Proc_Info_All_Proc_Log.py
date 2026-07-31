'''
Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, username.

Usage: Proc_Info_All_Proc.py Demo

Demo is the name of Directory.
'''

import psutil
import sys, os
import datetime
from zoneinfo import ZoneInfo
from File_Operations import WriteInFile

def show_greeting_init():
    return """======================================================================================
============================= Process Information Script =============================
======================================================================================

Script is started successfuly."""

def show_greeting_end():
    return """Script execution completed. Logs created in given directory.
    
======================================================================================
======================================================================================"""

def show_help():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Help:
This script accepts a directory name as input and creates a log file
inside that directory. The log file contains details of all running processes:
- Process Name
- Process ID (PID)
- Username
- Status

Syntax:
    python Proc_Info_All_Proc.py <directory_name>

Examples:
    python Proc_Info_All_Proc.py Demo
        Creates 'Demo/Process_31_07_2026_13_59_00.log' with process details

Notes:
    - You must provide a valid directory name.
    - Use --u for usage summary.
    - Use --h for detailed help.

======================================================================================
"""

def show_usage():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Usage: python Proc_Info_All_Proc.py <directory_name>

Description:
    Creates a log file in the specified directory.
    The log file contains information about all running processes:
    - Process Name
    - Process ID (PID)
    - Username
    - Status

Example:
    python Proc_Info_All_Proc.py Demo

======================================================================================
"""

def show_invalid():
    return """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Error: Invalid argument.

To see usage information, run:
    python Proc_Info_All_Proc.py --u
    or
    python Proc_Info_All_Proc.py --usage

To see detailed help, run:
    python Proc_Info_All_Proc.py --h
    or
    python Proc_Info_All_Proc.py --help

To execute the script, provide a directory name:
    python Proc_Info_All_Proc.py <directory_name>

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

get_proc_list = lambda : psutil.process_iter()

def monitor_process_details(dir_name):
    file_stamp = datetime.datetime.now().strftime("%d%m%Y_%I%M%S")
    file_name = os.path.join(dir_name, f"Proc_{file_stamp}.log")
    tz=ZoneInfo("Asia/Kolkata")

    WriteInFile(file_name, get_log_header(), "a")

    for proc in get_proc_list():
        log_text = ""
        try: 
            log_text = f"""
--------------------------------------------------------------------------------------
Process ID        : {proc.pid}
User Name         : {proc.username()}
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
    return

def main():
    options = sys.argv
    if(len(options) == 2 and (options[1] == "--h" or options[1] == "--help")):
        print(show_help())
    elif(len(options) == 2 and (options[1] == "--u" or options[1] == "--usage")):
        print(show_usage())
    elif(len(options) == 2):
        print(show_greeting_init())
        dir_name = options[1]
        monitor_process_details(dir_name)
        print(show_greeting_end())
    else:
        print(show_invalid())

if(__name__ == "__main__"):
    main()