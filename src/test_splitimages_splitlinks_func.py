import unittest
from textnode import TextNode, TextType
from extracts_funcs import *
from split_nodes_delimiter import *


class TestSplitNodesLink(unittest.TestCase):
    def test_basic_link(self):
        # Test with a single link
        nodes = [TextNode("This is a [link](https://example.com) in text", TextType.TEXT)]
        result = split_nodes_link(nodes)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://example.com")
        self.assertEqual(result[2].text, " in text")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_multiple_links(self):
        # Test with multiple links in text
        nodes = [TextNode("Start [link1](https://example1.com) middle [link2](https://example2.com) end", TextType.TEXT)]
        result = split_nodes_link(nodes)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Start ")
        self.assertEqual(result[1].text, "link1")
        self.assertEqual(result[1].url, "https://example1.com")
        self.assertEqual(result[2].text, " middle ")
        self.assertEqual(result[3].text, "link2")
        self.assertEqual(result[3].url, "https://example2.com")
        self.assertEqual(result[4].text, " end")
    
    def test_no_links(self):
        # Test with no links
        nodes = [TextNode("This text has no links", TextType.TEXT)]
        result = split_nodes_link(nodes)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This text has no links")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_non_text_nodes(self):
        # Test that non-TEXT nodes are left untouched
        nodes = [
            TextNode("Text [link](https://example.com)", TextType.TEXT),
            TextNode("Bold text", TextType.BOLD)
        ]
        result = split_nodes_link(nodes)
        
        # Modified: expecting 3 nodes instead of 4 (no empty text node)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text ")
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].url, "https://example.com")
        # No empty text node expected
        self.assertEqual(result[2].text, "Bold text")
        self.assertEqual(result[2].text_type, TextType.BOLD)
    
    def test_link_at_beginning(self):
        # Test with link at the beginning
        nodes = [TextNode("[link](https://example.com) after text", TextType.TEXT)]
        result = split_nodes_link(nodes)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "link")
        self.assertEqual(result[0].text_type, TextType.LINK)
        self.assertEqual(result[0].url, "https://example.com")
        self.assertEqual(result[1].text, " after text")
        self.assertEqual(result[1].text_type, TextType.TEXT)
    
    def test_link_at_end(self):
        # Test with link at the end
        nodes = [TextNode("Text before [link](https://example.com)", TextType.TEXT)]
        result = split_nodes_link(nodes)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Text before ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://example.com")


class TestSplitNodesImage(unittest.TestCase):
    def test_basic_image(self):
        # Test with a single image
        nodes = [TextNode("This is an ![image](https://example.com/img.png) in text", TextType.TEXT)]
        result = split_nodes_image(nodes)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://example.com/img.png")
        self.assertEqual(result[2].text, " in text")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_multiple_images(self):
        # Test with multiple images in text
        nodes = [TextNode("Start ![img1](https://example1.com/img1.png) middle ![img2](https://example2.com/img2.png) end", TextType.TEXT)]
        result = split_nodes_image(nodes)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Start ")
        self.assertEqual(result[1].text, "img1")
        self.assertEqual(result[1].url, "https://example1.com/img1.png")
        self.assertEqual(result[2].text, " middle ")
        self.assertEqual(result[3].text, "img2")
        self.assertEqual(result[3].url, "https://example2.com/img2.png")
        self.assertEqual(result[4].text, " end")
    
    def test_no_images(self):
        # Test with no images
        nodes = [TextNode("This text has no images", TextType.TEXT)]
        result = split_nodes_image(nodes)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This text has no images")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_non_text_nodes(self):
        # Test that non-TEXT nodes are left untouched
        nodes = [
            TextNode("Text ![image](https://example.com/img.png)", TextType.TEXT),
            TextNode("Bold text", TextType.BOLD)
        ]
        result = split_nodes_image(nodes)
        
        # Modified: expecting 3 nodes instead of 4 (no empty text node)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text ")
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].url, "https://example.com/img.png")
        # No empty text node expected
        self.assertEqual(result[2].text, "Bold text")
        self.assertEqual(result[2].text_type, TextType.BOLD)
    
    def test_image_at_beginning(self):
        # Test with image at the beginning
        nodes = [TextNode("![image](https://example.com/img.png) after text", TextType.TEXT)]
        result = split_nodes_image(nodes)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "image")
        self.assertEqual(result[0].text_type, TextType.IMAGE)
        self.assertEqual(result[0].url, "https://example.com/img.png")
        self.assertEqual(result[1].text, " after text")
        self.assertEqual(result[1].text_type, TextType.TEXT)
    
    def test_image_at_end(self):
        # Test with image at the end
        nodes = [TextNode("Text before ![image](https://example.com/img.png)", TextType.TEXT)]
        result = split_nodes_image(nodes)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Text before ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://example.com/img.png")


if __name__ == "__main__":
    unittest.main()