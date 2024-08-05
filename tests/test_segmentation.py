import unittest
from models.segmentation_model import segment_image

class TestSegmentation(unittest.TestCase):
    def test_segment_image(self):
        image_path = "../data/input_images/sample.jpg"
        image, prediction = segment_image(image_path)
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()
