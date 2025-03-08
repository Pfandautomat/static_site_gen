import unittest

from extracts_funcs import *


class TestExtractFuncs(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Test 1: Basic markdown image format
        text1 = "Here is an image ![alt text](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text1), [("alt text", "https://example.com/image.jpg")])
        
        # Test 2: Multiple images in text
        text2 = "First image ![first](https://example.com/1.jpg) and second image ![second](https://example.com/2.jpg)"
        self.assertEqual(extract_markdown_images(text2), [("first", "https://example.com/1.jpg"), 
                                                 ("second", "https://example.com/2.jpg")])
        
        # Test 3: Empty alt text
        text3 = "Image with no alt text ![](https://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text3), [("", "https://example.com/image.jpg")])
        
        # Test 4: Non-https URL (http)
        text4 = "Image with http ![alt](http://example.com/image.jpg)"
        self.assertEqual(extract_markdown_images(text4), [("alt", "http://example.com/image.jpg")])
        
        # Test 5: Malformed markdown - missing closing parenthesis
        text5 = "Malformed image ![alt](https://example.com/image.jpg"
        self.assertEqual(extract_markdown_images(text5), [])  # Current function would fail this test

if __name__ == '__main__':
    unittest.main()








