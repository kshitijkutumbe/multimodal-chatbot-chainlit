# app/utils.py
import base64
from logger import setup_logger

logger = setup_logger(__name__)

def image2base64(image_path):
    try:
        with open(image_path, "rb") as img:
            encoded_string = base64.b64encode(img.read())
        return encoded_string.decode("utf-8")
    except Exception as e:
        logger.error(f"Error encoding image to base64: {e}")
        raise
