import pytesseract
from .config import TESSERACT

if not pytesseract.pytesseract.tesseract_cmd:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT 