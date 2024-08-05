import unittest
from models.identification_model import identify_objects

class TestIdentification(unittest.TestCase):
    def test_identify_objects(self):
        object_image_path = "../data/segmented_objects/object_0.png"
        probs = identify_objects(object_image_path)
        self.assertIsNotNone(probs)

if __name__ == '__main__':
    unittest.main()
