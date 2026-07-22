'''

Write a python program that performs a file backup every hour.

The program should:
    1. Accept the source path.
    2. Accept the destination directory path.
    3. Copy the source file to the destination directory.
    4. Add the current date and time to the backup filename.
    5. Write the backup operation details into:
        backup_log.txt

Data_25_07_2026_16_30_00.txt

Backup completed successfully at 25-07-2026 04:30:00 PM
Use shutil module for file copying.

'''

import schedule, time, datetime, shutil, os, pathlib, sys

def WriteInFile(fileName, text):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, "a")
    fobj.write(text+"\n")
    fobj.close()

backup_timeStamp = lambda : datetime.datetime.now().strftime("%d_%m_%Y_%I_%M_%S")
logs_timestamp = lambda : datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
log_text_success = lambda : f"Backup completed successfully at {logs_timestamp()}"
log_text_failure = lambda : f"Backup failed - source file not found: {logs_timestamp()}"
write_in_log = lambda isSuccess: WriteInFile("Logs/backup_log.txt", log_text_success() if isSuccess else log_text_failure())

def CopyFile(src, dst_dir):
    if (not os.path.exists(src)):
        print(f"Source file '{src}' not found")
        write_in_log(isSuccess=False)
        return

    dst = f"{dst_dir}/Data_{backup_timeStamp()}.txt"
    path = pathlib.Path(dst)
    path.parent.mkdir(parents=True, exist_ok=True)
    print("src: ", src, "\ndst: ", path)
    shutil.copyfile(src, path)
    write_in_log(isSuccess=True)
    print("Backup completed: ", datetime.datetime.now().ctime())


def main():

    border = "-"*60
    print(border)
    print("Marvellous Infosystem Script.")
    print(border)

    if(len(sys.argv) == 3):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Please execute script as: ")
            print("python '<fileName>'.py '<source file path to be backed up>' <destination path for backup>")
            print("For better usage, please check --u flag")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("This automation script is used to backup the data file.")
            print("Paths should be absolute path")

        else:
            src = pathlib.Path(sys.argv[1].replace("\\", "/"))
            dst_dir = str(pathlib.Path(sys.argv[2].replace("\\", "/")))
            schedule.every(1).hours.do( lambda : CopyFile(src, dst_dir))

            while True:
                schedule.run_pending()
                # time.sleep(1)
    else:
        print("Invalid Arguments")
        print("Please use --u or --h for more information.")
    
    print(border)
    print("Thank you for using Marvellous Infosystem Script.")
    print(border)

if __name__ == "__main__":
    main()