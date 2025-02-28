import os
import requests
from dotenv import load_dotenv
import logging
__name__ = "__image_compressor__"
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()


# Environment variables (should be set in your system)
API_KEYS = {
    'tinypng': os.getenv('tinify_api_key')
}


def compress_image(file_path: str) -> str:
    """
    Compress PNG/JPG using TinyPNG API.
    
    Example call:
    compress_image("/path/to/image.png")

    Args:
        file_path (str): Path to image file (PNG or JPG)

    Returns:
        str: Path to compressed image file

    Raises:
        Exception: If API request fails or non-image file
    """
    try:
        url = 'https://api.tinify.com/shrink'
        auth = ('api', API_KEYS['tinypng'])
        
        logger.info("Started communicating with TinyPNG online service to compress the given input image..")

        with open(file_path, 'rb') as f:
            response = requests.post(url, auth=auth, data=f.read())
            
        if response.status_code == 201:
            logger.info("Processed and compressed the given input image successfully.....")
            b = file_path.split(".")[0]
            output_path = f"{b}_compressed.png"
            with open(output_path, 'wb') as f:
                f.write(requests.get(response.json()['output']['url']).content)
                logger.info("Saved the resultant compressed image successfully...")

            return output_path
        
    except Exception as e:
        logger.info(f"Image compression failed: {str(e)}")
