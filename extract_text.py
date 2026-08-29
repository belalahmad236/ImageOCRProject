import os
from PIL import Image
import pytesseract

# Path to Tesseract executable (update if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Folder containing images
image_folder = "images"

# Output file to store extracted text
output_file = "extracted_text.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for idx, file in enumerate(os.listdir(image_folder), start=1):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(image_folder, file)
            try:
                text = pytesseract.image_to_string(Image.open(image_path))
                f.write(f"--- {file} ---\n{text}\n\n")
                print(f"[{idx}] Processed: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

print(f"\n✅ Extraction complete! Text saved to {output_file}")
