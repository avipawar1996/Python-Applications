'''
Design automation script which accept process name and display information of that process if it is running.

Usage: Proc_Info_All_Proc.py Notepad

'''

import psutil
import sys
import datetime
from zoneinfo import ZoneInfo

def show_greeting_init():
    return """======================================================================================
============================= Process Information Script =============================
======================================================================================

"""

def show_greeting_end():
    return """
======================================================================================
======================================================================================"""

def show_help():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Help:
This script checks if a given process is currently running.

Syntax:
    python Proc_Check_ProcName.py <process_name>

Examples:
    python Proc_Check_ProcName.py notepad.exe   : Tells if 'notepad' is running
    python Proc_Check_ProcName.py python.exe    : Tells if 'python' is running

Notes:
    - You must provide a process name as an argument.
    - Use --u for usage summary.
    - Use --h for detailed help.

======================================================================================
"""

def show_usage():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Usage: python Proc_Check_ProcName.py <process_name>

Options:
    --u, --usage    Show usage information
    --h, --help     Show help information

Example:
    python Proc_Check_ProcName.py chrome.exe

======================================================================================
"""

def show_invalid():
    return """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Error: Invalid argument passed.

To see usage information, run:
    python Proc_Check_ProcName.py --u
    or
    python Proc_Check_ProcName.py --usage

To see detailed help, run:
    python Proc_Check_ProcName.py --h
    or
    python Proc_Check_ProcName.py --help

======================================================================================
"""

get_proc_list = lambda : psutil.process_iter()

def monitor_process_details(proc_name):
    tz=ZoneInfo("Asia/Kolkata")
    is_found = False
    matched_proc = None
    # proc_name = str(proc_name)
    proc_list = get_proc_list()
    for proc in proc_list:
        if(proc_name.lower() in  proc.name().lower()):
            is_found = True
            matched_proc = proc
            break

    if is_found == True:
        print("Process ID        : ", matched_proc.pid)
        print("User Name         : ", matched_proc.username())
        print("Process Name      : ", matched_proc.name())
        print("Process Status    : ", matched_proc.status())
        print("Process Started   : ", datetime.datetime.fromtimestamp(matched_proc.create_time(), tz=tz))
    else:
        print(f"Process with name '{proc_name}' is not running.")

def main():
    options = sys.argv
    if(len(options) == 2 and (options[1] == "--h" or options[1] == "--help")):
        print(show_help())
    elif(len(options) == 2 and (options[1] == "--u" or options[1] == "--usage")):
        print(show_usage())
    elif(len(options) == 2):
        print(show_greeting_init())
        proc_name = options[1]
        monitor_process_details(proc_name)
        print(show_greeting_end())
    else:
        print(show_invalid())

if(__name__ == "__main__"):
    main()