import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_split(self):
        # Test basic splitting with a single delimiter pair
        input_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_no_delimiter(self):
        # Test with text that doesn't contain the delimiter
        input_nodes = [TextNode("This has no delimiter", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This has no delimiter")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    

    
    def test_non_text_nodes(self):
        # Test that non-TEXT nodes are preserved unchanged
        input_nodes = [
            TextNode("Normal text", TextType.TEXT),
            TextNode("Already bold", TextType.BOLD),
            TextNode("Text with **delimiter**", TextType.TEXT)
        ]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Normal text")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Already bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, "Text with ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "delimiter")
        self.assertEqual(result[3].text_type, TextType.BOLD)
    
    def test_odd_number_of_delimiters(self):
        # Test handling of text with an odd number of delimiters
        input_nodes = [TextNode("Text with **unpaired delimiter", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "unpaired delimiter")
        self.assertEqual(result[1].text_type, TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
