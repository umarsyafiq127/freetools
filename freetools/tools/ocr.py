import pytesseract
from PIL import Image
import io
import os

# Jika di Windows, tentukan path Tesseract secara manual
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text if text.strip() else "Teks tidak ditemukan atau tidak terbaca."

print(f"OCR bisa")