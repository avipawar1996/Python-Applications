# built-in/pip modules import
import sys
import os
import datetime, time
import multiprocessing
import schedule

# User defined modules Import
from Directory_Operations import validate_dir, dir_scanner, find_duplicate
from File_Operations import calculate_checksum, WriteInFile
from Email_Service import send_email, validate_email

def get_time_stamp(): return datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def remove_duplicate(dir_path, rec_email):
    log_file_name = f"Logs/DuplicateRemovalLog_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

    num_of_files_deleted = 0 
    file_list = list()
    files_for_deletion = list()
    email_send_status = False
    is_email_sender_valid = validate_email_sender()

    # Write log, sanitizer run started
    log_text = """
========================================================================================
============================== Disk Sanitizer Run Started ==============================
========================================================================================


"""
    WriteInFile(log_file_name, log_text, "a")

    started_at = get_time_stamp()
    log_text = f"Scan Started at: {started_at}\n"

    WriteInFile(log_file_name, log_text, "a")

    # Validat the directory for is a valid path? is a dir path? is having permission for the path given? 
    validate_dir_res = validate_dir(dir_path)
    isValidPath = validate_dir_res[0]
    dirValidationError = validate_dir_res[1]
    is_email_valid = validate_email(rec_email)

    if(is_email_valid):
        log_text = f"Email Address validation is successful.\n"
        WriteInFile(log_file_name, log_text, "a")
    else:
        log_text = f"Provided Email Address is invalid.\n"
        WriteInFile(log_file_name, log_text, "a")

    if(isValidPath == False):
        log_text = f"{get_time_stamp()} - Directory validation Failed: {dirValidationError}\n"
        log_text = log_text + f"'{dir_path}'\n"
        WriteInFile(log_file_name, log_text, "a")

    else:
        # List the files present in given directory recursively
        file_list = dir_scanner(dir_path)

        log_text = f"""
Path of directory scanned: '{dir_path}'
Number of files scanned: {len(file_list)}

"""
        WriteInFile(log_file_name, log_text, "a")


        # Checksum calculate method will return result object as :
        # result = {
        #     "filePath": file_path,
        #     "checksum": None,
        #     "isSuccess": False,
        #     "error": None
        # }
        # Handling below the success/failure in finding checksum of file present in list

        checksum_success = list()
        checksum_failure = list()

        for fileName in file_list:
            # Pass file path to checksum utility and collect checksum response object
            checksum_result = calculate_checksum(fileName)

            # If checksum is successful, filter it in checksum_success list as {"checksum": <file checksum>, filePath: <file path> }
            if(checksum_result["isSuccess"] == True):
                checksum_success.append({
                    "filePath" : checksum_result["filePath"],
                    "checksum" : checksum_result["checksum"]
                })

            # If checksum utility falied, put the response error object in checksum_error for error handling
            else:
                checksum_failure.append({
                    "filePath" : checksum_result["filePath"],
                    "error" : checksum_result["error"],
                })

                log_text = f"Checksum failed for: \nFile Path: {fileName}: \nError: {checksum_result['error']}\n"

        # find_duplicate returns mapped dictionary as: [{checksum : [list of files with same checksum (duplicate content)]}]
        duplicate_files_mapped_list = find_duplicate(checksum_success)

        # Prepare the final list of files to be deleted (files that has same checksum)
        num_of_duplicate = 0
        for checksum_key, filePathList in duplicate_files_mapped_list.items():
            num_of_files = len(filePathList)
            # More than one files having same checksum : keep 1st include remaining for deletion
            if( num_of_files > 1):
                for file in range(1, num_of_files):
                    num_of_duplicate = num_of_duplicate + 1
                    files_for_deletion.append({
                        "checksum_key": checksum_key , "file_path": filePathList[file]
                    })

        # If duplicate files found for deletion then write related logs in log gile
        if(len(files_for_deletion) > 0):


            log_text = f"""
---------------------------- Duplicate File Deletion Status ----------------------------

"""
            WriteInFile(log_file_name, log_text, "a")

            for file_to_delete in files_for_deletion:
                try:
                    os.remove(file_to_delete["file_path"])
                    WriteInFile(log_file_name, f"Deleted File: '{file_to_delete["file_path"]}'\n", "a")
                    WriteInFile(log_file_name, f"File Checksum: {file_to_delete["checksum_key"]}", "a")

                    num_of_files_deleted = num_of_files_deleted + 1

                    log_text = """

----------------------------------------------------------------------------------------
"""
                    WriteInFile(log_file_name, log_text, "a")

                except Exception as e:
                    if (not os.path.exists(file_to_delete["file_path"])):
                        num_of_files_deleted = num_of_files_deleted + 1
                        WriteInFile(log_file_name, f"Deleted with warning: '{file_to_delete["file_path"]}'\n", "a")
                        WriteInFile(log_file_name, f"Checksum: {file_to_delete["file_path"]}", "a")

                        num_of_files_deleted = num_of_files_deleted + 1
                        log_text = """

----------------------------------------------------------------------------------------
"""
                        WriteInFile(log_file_name, log_text, "a")
                    else:
                        WriteInFile(log_file_name, f"Failed to Delete: {file_to_delete["file_path"]}: {e}", "a")
                        num_of_files_deleted = num_of_files_deleted + 1
                        log_text = """

----------------------------------------------------------------------------------------
"""
                        WriteInFile(log_file_name, log_text, "a")

            log_text = f"Total number of duplicate files found: {len(files_for_deletion)}\n"
            WriteInFile(log_file_name, log_text, "a")
            
        else:
            log_text = f"No duplicate files found for deletion: {get_time_stamp()}\n"
            WriteInFile(log_file_name, log_text, "a")

    completed_at = get_time_stamp()

    log_text = f"\nScan Completed at: {get_time_stamp()}"
    WriteInFile(log_file_name, log_text, "a")

    if(is_email_valid and is_email_sender_valid):
        sender_email = os.environ.get("app_email")
        password = os.environ.get("app_password")
        
        if(sender_email == None or password == None):
            log_text = f"\nEmail Address and Password not set in user environment variable or not matching. Email cannot be sent.\n"
            WriteInFile(log_file_name, log_text, "a")
        
        receipent_email = rec_email
        email_subject = f"Disk Sanitizer Scan : {get_time_stamp()}"
        email_body = f"""
    Jay Ganesh,

    The duplicate file removal operation has been completed successfully.
    Starting time of scanning: {started_at}
    Completion time of scanning: {completed_at}
    Directory Scanned: '{dir_path}'
    Directory Validation: {'Valid' if isValidPath else dirValidationError}
    Total Number of files scanned: {0 if not len(file_list) else len(file_list)}
    Total number of duplicate files found: {0 if not len(files_for_deletion) else len(files_for_deletion)}
    Total number of files deleted: {num_of_files_deleted}

    Please find detailed log file attached to this email.

    Regards,
    Avinash Pawar
    """
        attachment = [os.path.abspath(log_file_name)]
        if is_email_sender_valid: 
            email_send_status = send_email(
                sender_email,
                password,
                receipent_email,
                email_subject,
                email_body,
                attachment
            )

    
    log_text = f"""
Email state: {"Invalid sender credentials. Please check in user environment variables."
              if not is_email_sender_valid
              else ("Not sent. Provided email address is not valid."
                    if not is_email_valid
                    else ("Sent" if email_send_status else "Failed")) }

========================================================================================
===============================  Directory Scan Completed  =============================
========================================================================================
"""
    WriteInFile(log_file_name, log_text, "a")

def printBorder(msg):
    print(f"-"*70)
    print(msg)
    print(f"-"*70)

def print_help(script_name):
    display_msg = f"""

Duplicate File Removal Automation - Help

This script scans a directory, identifies duplicate files using checksum,
removes duplicates, creates a detailed log file, and emails the log report.

Usage:
    python {script_name} <directory_path> <intervalInMinutes> <receiver_email>

Arguments:
    <directory_path>     Full path of the directory to be scanned
    <intervalInMinutes>  Time interval (in minutes) to repeat the scan
    <receiver_email>     Email address to receive the log report

Options:
    --h, --help          Show this help message
    --u, --usage         Show usage information

"""
    print(display_msg)

def print_usage(script_name):
    display_msg = f"""
Duplicate File Removal Automation - Usage

Example:
    python {script_name} r'C:/Users/Avinash/Documents' 30 avi1996pawar@gmail.com

Explanation:
    - The script will scan the given directory every 30 minutes
    - Duplicate files (based on checksum) will be deleted
    - A log file will be generated for each run
    - The log file will be emailed to avi1996pawar@gmail.com
"""
    print(display_msg)

def print_invalid(script_name):
    display_msg = f"""
Invalid Parameters!

Usage:
    python Disk_Sanitizer.py <directory_path> <intervalInMinutes> <receiver_email>

Arguments:
    <directory_path>     Full path of the directory to be scanned
    <intervalInMinutes>  Time interval (in minutes) to repeat the scan
    <receiver_email>     Email address to receive the log report

Examples:
    python {script_name} r'C:/Users/Avinash/Documents' 30 avi1996pawar@gmail.com

Notes:
    - All three arguments are required
    - <intervalInMinutes> must be a positive integer
    - <receiver_email> must be a valid email address
"""
    print(display_msg)

def validate_email_sender():
    for env_var in ["app_email", "app_password"]:
        if os.environ.get(env_var) is None:
            print(env_var, ": None")
            return False
    return True

def main():

    printBorder("Disk Sanitizer")

    if(len(sys.argv) == 2):

        if(sys.argv[1].lower() == "--h" or sys.argv[1].lower() == "--help"):
            print_help(sys.argv[0])
            printBorder("Thank You for using Disk Sanitizer")
            return

        if(sys.argv[1].lower() == "--u" or sys.argv[1].lower() == "--usage"):
            print_usage(sys.argv[0])
            printBorder("Thank You for using Disk Sanitizer")
            return

    elif(len(sys.argv) == 4):

        # Collecting command line arguments for directory path and interval
        dir_path = sys.argv[1]
        interval = sys.argv[2]
        rec_email = sys.argv[3]

        try:
            interval = int(interval)
        except Exception as e:
            print("\n Entered time interval is not valid \n\n")
            printBorder("Thank You for using Disk Sanitizer")
            return

        # calling duplicate removal method
        schedule.every(interval).minutes.do(lambda : remove_duplicate(dir_path, rec_email))

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt as ke:
            printBorder("Disk Sanitizer stopped by user")

        printBorder("Thank You for using Disk Sanitizer")

    else:
        print_invalid(sys.argv[0])
        printBorder("\n\nThank You for using Disk Sanitizer")
    return



if(__name__ == "__main__"):
    main()