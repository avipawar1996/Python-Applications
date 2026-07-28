
import os

def validate_dir(dir_path):

    if (not os.path.isabs(dir_path)):
        return (False, f"Directory path must be an absolute path")

    if (not os.path.exists(dir_path)):
        return (False, "Directory does not exist")

    if (not os.path.isdir(dir_path)):
        return (False, f"Path is not a directory: {dir_path}")
    
    if (not os.path.isdir(dir_path)):
        return (False, f"Directory does not exist: {dir_path}")

    if (not os.access(dir_path, os.R_OK | os.X_OK)):
        return (False, f"No read/execute permission for this directory: {dir_path}")

    else: return True, None

def dir_scanner(dir_path):
    file_list = list()
    for dirPath,  subDirs, fileNames in os.walk(dir_path):
        for fileName in fileNames:
            file_list.append(os.path.join(dirPath, fileName))

    return file_list

def find_duplicate(file_checksum_list):
    duplicate = {}

    for file_checksum_obj in file_checksum_list:
        if(file_checksum_obj["checksum"] in duplicate):
            duplicate[file_checksum_obj["checksum"]].append(file_checksum_obj["filePath"])
        else:
            duplicate[file_checksum_obj["checksum"]] = [file_checksum_obj["filePath"]]
    return duplicate