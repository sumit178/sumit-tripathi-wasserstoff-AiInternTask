import unittest
from models.summarization_model import summarize_text

class TestSummarization(unittest.TestCase):
    def test_summarize_text(self):
        text = "The cat is sitting on the mat. It looks very happy and comfortable."
        summary = summarize_text(text)
        self.assertIsNotNone(summary)

if __name__ == '__main__':
    unittest.main()
