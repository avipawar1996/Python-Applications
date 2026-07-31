'''
Design automation script which display information of running processes as its name, pid, username.
Usage: Proc_Info_All_Proc.py
'''

import psutil
import sys
import datetime

def show_help():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Help:
This script displays information about all running processes,
including process name, PID, and username.

Examples:
    python Proc_Info_All_Proc.py        : List all processes
    python Proc_Info_All_Proc.py --u    : Show usage summary
    python Proc_Info_All_Proc.py --h    : Show detailed help

======================================================================================
"""

def show_greeting_init():
    return """======================================================================================
============================= Process Information Script =============================
======================================================================================

Script is started successfuly."""

def show_greeting_end():
    return """Script execution completed.
======================================================================================
======================================================================================"""

def show_usage():
    return  """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Usage: python Proc_Info_All_Proc.py [option]

Options:
    --u, --usage    Show usage information
    --h, --help     Show help information

Run without arguments to list all processes.

======================================================================================
"""

def show_invalid():
    return """
======================================================================================
============================= Process Information Script =============================
======================================================================================

Error: Invalid arguments provided.

To see usage information, run:
    python Proc_Info_All_Proc.py --u
    or
    python Proc_Info_All_Proc.py --usage

To see detailed help, run:
    python Proc_Info_All_Proc.py --h
    or
    python Proc_Info_All_Proc.py --help

======================================================================================
"""

def get_process_details():
    return psutil.process_iter()

def monitor_proc():
    proc_list = get_process_details()
    try:
        for proc in proc_list:
            print("------------------------------------------------------------------------")
            print("Process ID        : ", proc.pid)
            print("Process Name      : ", proc.name())
            print("User Name         : ", proc.username())
            print("Process Status    : ", proc.status())
            print("------------------------------------------------------------------------")
    except Exception as e:
        print("------------------------------------------------------------------------")
        print(f"ERROR: {e}")
        print("------------------------------------------------------------------------")

def main():
    options = sys.argv
    if(len(options) == 1):
        print(show_greeting_init())
        monitor_proc()
        print(show_greeting_end())
    if(len(options) == 2 and (options[1] == "--h" or options[1] == "--help")):
        print(show_help())
    if(len(options) == 2 and (options[1] == "--u" or options[1] == "--usage")):
        print(show_usage())
    else:
        print(show_invalid())

if(__name__ == "__main__"):
    main()