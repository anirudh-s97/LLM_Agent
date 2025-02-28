import os
import requests
from dotenv import load_dotenv

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
        print(API_KEYS["tinypng"])
        auth = ('api', API_KEYS['tinypng'])
        
        with open(file_path, 'rb') as f:
            response = requests.post(url, auth=auth, data=f.read())
            
        if response.status_code == 201:
            b = file_path.split(".")[0]
            output_path = f"{b}_compressed.png"
            with open(output_path, 'wb') as f:
                f.write(requests.get(response.json()['output']['url']).content)
            return output_path
            
        raise Exception(f"Image compression failed: {response.text}")
        
    except Exception as e:
        raise Exception(f"Image processing error: {str(e)}")
