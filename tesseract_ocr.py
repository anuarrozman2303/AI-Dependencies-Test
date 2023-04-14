from pytesseract import image_to_string
from PIL import Image
image_to_string(Image.open('ocr_1.png'))