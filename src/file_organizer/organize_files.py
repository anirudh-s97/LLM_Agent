import os
import shutil
from typing import Dict, List


def move_files_to_categories(source_dir: str, 
                            destination_root: str = None) -> None:
    """
    Organize files into category-specific directories.
    
    Example call:
    move_files_to_categories("/source/path", {"file.pdf": "PDFs"}, "/destination/path")
    
    Args:
        source_dir (str): Directory containing original files
        file_category_mapping (Dict[str, str]): Filename to category mapping
        destination_root (str, optional): Base directory for categorized folders.
            Defaults to source_dir if not provided.
            
    Returns:
        None
    """

    dest_map = {}

    category_map = {
        # Document formats
        'pdf': 'PDFs',
        'doc': 'Documents', 'docx': 'Documents', 'odt': 'Documents',
        'rtf': 'Documents', 'tex': 'Documents',
        
        # Image formats
        'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images',
        'gif': 'Images', 'bmp': 'Images', 'svg': 'Images',
        'tiff': 'Images', 'webp': 'Images',
        
        # Code formats
        'py': 'Code Files', 'js': 'Code Files', 'java': 'Code Files',
        'cpp': 'Code Files', 'c': 'Code Files', 'h': 'Code Files',
        'html': 'Code Files', 'css': 'Code Files', 'php': 'Code Files',
        'rb': 'Code Files', 'swift': 'Code Files', 'kt': 'Code Files',
        
        # Data formats
        'csv': 'Data', 'json': 'Data', 'xml': 'Data', 'yaml': 'Data',
        'yml': 'Data', 'db': 'Data', 'sql': 'Data',
        
        # Archive formats
        'zip': 'Archives', 'tar': 'Archives', 'gz': 'Archives',
        '7z': 'Archives', 'rar': 'Archives', 'xz': 'Archives',
        
        # Spreadsheet formats
        'xls': 'Spreadsheets', 'xlsx': 'Spreadsheets', 'ods': 'Spreadsheets',
        
        # Text formats
        'txt': 'Text Files', 'md': 'Text Files', 'log': 'Text Files',
        
        # Media formats
        'mp3': 'Media', 'mp4': 'Media', 'avi': 'Media', 'mov': 'Media',
        'wav': 'Media', 'flac': 'Media', 'mkv': 'Media',
        
        # Executable formats
        'exe': 'Executables', 'msi': 'Executables', 'app': 'Executables',
        'dmg': 'Executables'
    }

    file_categories = {}
    for filename in os.listdir(source_dir):
        # Split filename and handle hidden/unix-style files
        _, _, ext = filename.rpartition('.')
        ext = ext.lower()
        category = category_map.get(ext, 'Other')
        file_categories[filename] = category

    if not destination_root:
        destination_root = os.path.join(os.path.dirname(source_dir), "organized_data")
        os.makedirs(destination_root, exist_ok=True)

    # Create all category directories first
    categories = set(file_categories.values())
    for category in categories:
        os.makedirs(os.path.join(destination_root, category), exist_ok=True)

    # Move files to their categories
    for filename, category in file_categories.items():
        src_path = os.path.join(source_dir, filename)
        dest_dir = os.path.join(destination_root, category)

        dest_map[filename] = os.path.join(dest_dir, filename)
        
        try:
            shutil.move(src_path, dest_dir)
        except shutil.Error as e:
            print(f"Couldn't move {filename}: {str(e)}")
        except FileNotFoundError:
            print(f"Source file not found: {filename}")

    return dest_map
