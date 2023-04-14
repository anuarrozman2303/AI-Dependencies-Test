from pytesseract import image_to_string
from PIL import Image
image = Image.open('ocr_1.png')

text = image_to_string(image)

print(text)