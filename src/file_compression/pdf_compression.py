import os
import logging
from dotenv import load_dotenv
from pylovepdf.tools.compress import Compress
import os

load_dotenv()
__name__ = "__pdf_compressor__"

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

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

        logger.info("Sending the pdf to Online Service to Compress it.....")  

        t = Compress(API_KEYS["ilovepdf"], verify_ssl=True, proxies=False)
        t.add_file(file_path)
        t.set_output_folder(output_path)
        t.execute()
        logger.info("Compression task executed successfully!!!!")
        t.download()
        t.delete_current_task()
        logger.info("Downloaded and saved the comprressed pdf successfully in the respective folder...")
        
            
        return output_path
        
    except Exception as e:
        logger.info(f"PDF compression failed: {str(e)}")
