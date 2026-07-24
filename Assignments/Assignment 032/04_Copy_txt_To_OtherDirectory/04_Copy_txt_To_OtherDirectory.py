"""
Write a program that copies all .txt files from one directory to another every ten miunutes.

The program should:
    Accept source and destination directories
    Validate both directories
    Copy only .txt files
    Maintain log of copied files
    Avoid terminating if one file cannot be copied
"""

import sys, os, time, schedule, datetime,pathlib, shutil

GetLogFileName = lambda : f"Logs/FileCopyLog.txt"
getLogText = lambda srcFileFullPath: f"""
-------------------------------------------------------------------------
    FilePath: {srcFileFullPath}
    Monitoring Date & Time: {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}
    File Size ib Bytes: {os.path.getsize(srcFileFullPath)}
-------------------------------------------------------------------------
"""

getTimeStamp = lambda : datetime.datetime.now().strftime("%d%m%Y_%H%M%S")

def WriteInFile(fileName, text):
    path = pathlib.Path(fileName)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, "a")
    fobj.write(text)
    fobj.close()

def CopyFilesRecursively(src, dest, fileExtn):
    border = "-" * 90
    logText = border
    for dirName, subDirNames, fileNames in os.walk(src):
        for fileName in fileNames:
            if(str(fileName).endswith(fileExtn)):
                srcAbsPath = os.path.abspath(pathlib.Path(os.path.join(dirName, fileName)))

                relPath = os.path.relpath(dirName, src)
                destAbsDirPath = os.path.join(os.path.abspath(dest), getTimeStamp(), relPath)
                destAbsPath = os.path.join(destAbsDirPath, fileName)
                pathlib.Path(destAbsDirPath).mkdir(parents=True, exist_ok=True)
                shutil.copyfile(srcAbsPath, destAbsPath)

                logText = logText + "\n" + srcAbsPath

    logText = logText + "\n" + border

    print(logText)
    WriteInFile("Logs/FileCopyLog.txt", logText)
    print("Copying completed..")

def main():
    border = "-"*70
    print(border)
    print("Marvellous Infosystem File Backup Script")
    print(border)

    if(len(sys.argv) > 1):
        if (sys.argv[1]== "--H" or sys.argv[1]== "--h"):
            print("Run the script as: 'python <scriptname.py> <sourcedir> <destination dir>'")
            print("To know the usage, please run 'python <scriptname.py> --u'")

            ExitBorderPrint()
            return

        elif (sys.argv[1]== "--U" or sys.argv[1]== "--u"):
            print("This script create the backup of all txt files present in given source directory to destination path following source directory structure.")

            ExitBorderPrint()
            return

        if(len(sys.argv) == 3):
            srcDir = sys.argv[1]
            destDir = sys.argv[2]

            for dir in [srcDir, destDir]:
                if(not os.path.exists(dir)):
                    print("Directory not exist: ", dir)
                    ExitBorderPrint()
                    return
            
            schedule.every(10).minutes.do(lambda : CopyFilesRecursively(srcDir, destDir, ".txt"))
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
    print("Thank You for using Marvellous Infosystem File Backup Script.")
    print(border)

if(__name__ == "__main__"):
    main()