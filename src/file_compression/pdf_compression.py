import os
from dotenv import load_dotenv
from pylovepdf.tools.compress import Compress
import os

load_dotenv()


# Environment variables (should be set in your system)
API_KEYS = {
    'ilovepdf': os.getenv('public_key')
}


def compress_pdf(file_path: str) -> str:
    """
    Compress PDF using ILovePDF API.
    
    Example call:
    compress_pdf("/path/to/document.pdf", "/path/to/output")

    Args:
        file_path (str): Path to the input PDF file
        output_dir (str): Directory to save compressed PDF

    Returns:
        str: Path to compressed PDF file

    Raises:
        Exception: If API request fails or invalid response
    """
    try:
        output_path = os.path.join(os.path.dirname(file_path), f'compressed_{os.path.basename(file_path)}')        

        t = Compress(API_KEYS["ilovepdf"], verify_ssl=True, proxies=False)
        t.add_file(file_path)
        t.set_output_folder(output_path)
        t.execute()
        t.download()
        t.delete_current_task()
        
            
        return output_path
        
    except Exception as e:
        raise Exception(f"PDF compression failed: {str(e)}")
