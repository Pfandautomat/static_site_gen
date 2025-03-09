import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        # Test with plain text without any markdown
        text = "This is just plain text"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is just plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_bold_text(self):
        # Test with bold markdown
        text = "This has **bold** text"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This has ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_italic_text(self):
        # Test with italic markdown
        text = "This has _italic_ text"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This has ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_code_text(self):
        # Test with code markdown
        text = "This has `code` text"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This has ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_link(self):
        # Test with a link
        text = "This has a [link](https://example.com) in it"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This has a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://example.com")
        self.assertEqual(nodes[2].text, " in it")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_image(self):
        # Test with an image
        text = "This has an ![image](https://example.com/img.png) in it"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This has an ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://example.com/img.png")
        self.assertEqual(nodes[2].text, " in it")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_multiple_formats(self):
        # Test with multiple markdown formats
        text = "**Bold**, _italic_, and `code` with a [link](https://example.com)"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes[0].text, "Bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text, ", ")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, "italic")
        self.assertEqual(nodes[2].text_type, TextType.ITALIC)
        self.assertEqual(nodes[3].text, ", and ")
        self.assertEqual(nodes[3].text_type, TextType.TEXT)
        self.assertEqual(nodes[4].text, "code")
        self.assertEqual(nodes[4].text_type, TextType.CODE)
        self.assertEqual(nodes[5].text, " with a ")
        self.assertEqual(nodes[5].text_type, TextType.TEXT)
        self.assertEqual(nodes[6].text, "link")
        self.assertEqual(nodes[6].text_type, TextType.LINK)
        self.assertEqual(nodes[6].url, "https://example.com")
    
    def test_nested_formats(self):
        # Test with nested formatting (should process outer format)
        text = "This has **_nested_** formatting"
        nodes = text_to_textnodes(text)
        
        # The expected behavior depends on your implementation
        # This test assumes that the bold delimiter is processed first
        self.assertEqual(nodes[0].text, "This has ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "_nested_")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " formatting")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_empty_text(self):
        # Test with empty text
        text = ""
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()