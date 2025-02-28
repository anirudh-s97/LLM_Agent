import os
from typing import Dict, List
import logging
__name__ = "__folder_scanner__"
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

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
        logging.info("The Folder Path you have shared is empty")
        logging.info("Please give a folder path that has files to process")
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
        logger.info("The path you have entered either doesn't exist or there are no files in the folder to process.")
        check = False
    
    return check