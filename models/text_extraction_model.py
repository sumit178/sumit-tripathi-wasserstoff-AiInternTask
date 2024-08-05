import pytesseract
from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    object_image_path = "../data/segmented_objects/object_0.png"
    text = extract_text(object_image_path)
    print(text)
