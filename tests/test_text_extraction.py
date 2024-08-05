import unittest
from models.text_extraction_model import extract_text

class TestTextExtraction(unittest.TestCase):
    def test_extract_text(self):
        object_image_path = "../data/segmented_objects/object_0.png"
        text = extract_text(object_image_path)
        self.assertIsNotNone(text)

if __name__ == '__main__':
    unittest.main()
