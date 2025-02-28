import os
from typing import Dict, List

def scan_folder(directory: str) -> List[str]:
    """
    Scan a directory and return a list of contained filenames.
    
    Example call:
    scan_folder("/path/to/directory")
    
    Args:
        directory (str): Path to the target directory to scan
        
    Returns:
        List[str]: List of filenames found in the directory. Returns empty list
        if directory doesn't exist or contains no files.
    """

    files = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.name)
    except FileNotFoundError:
        return []
    return files


def validate_folder_and_files(folder_path: str) -> bool:
    """
    Check whether a particular folder is present or not.
    Iteratively checks if any file is present in a folder or not.

    Example call:
    validate_folder_and_files(/path/to/folder)

    Args:
        folder_path: Path to the folder

    Returns:
        Return True if the folder exists and there are some files to process else False

    """

    check = True

    if not os.path.exists(folder_path) or os.listdir(folder_path) == []:
        check = False
    
    return check