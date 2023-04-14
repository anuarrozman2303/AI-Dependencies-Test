from pytesseract import image_to_string
import Imaage
print image_to_string(Image.open('ocr.png'))