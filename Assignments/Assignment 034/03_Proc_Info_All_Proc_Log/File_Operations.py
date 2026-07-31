import hashlib, pathlib

def calculate_checksum(file_path):
    result = {
        "filePath": file_path,
        "checksum": None,
        "isSuccess": False,
        "error": None
    }
    try:
        hlib = hashlib.md5()
        fobj = open(file_path, "rb")

        buffer = fobj.read(1024)
        while(len(buffer) > 0):
            hlib.update(buffer)
            buffer = fobj.read(1024)

        result["checksum"] = hlib.hexdigest()
        result["isSuccess"] = True

    except PermissionError:
        result["error"] = "PermissionError"
    except FileNotFoundError:
        result["error"] = "FileNotFoundError"
    except Exception as e:
        result["error"] = f"Error: {e}"

    return result

def WriteInFile(file_name, file_content, mode="r"):
    path = pathlib.Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    fobj = open(path, mode=mode)
    fobj.write(file_content)
    fobj.close()