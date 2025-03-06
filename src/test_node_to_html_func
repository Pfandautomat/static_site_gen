import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from text_to_html import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_text_to_html_node_text(self):
        # Test converting a plain TEXT node
        text_node = TextNode("This is plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is plain text")
        self.assertEqual(html_node.to_html(), "This is plain text")
    
    def test_text_to_html_node_bold(self):
        # Test converting a BOLD node
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")
    
    def test_text_to_html_node_italic(self):
        # Test converting an ITALIC node
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")
    
    def test_text_to_html_node_code(self):
        # Test converting a CODE node
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")
    
    def test_text_to_html_node_link(self):
        # Test converting a LINK node
        text_node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})
        self.assertEqual(html_node.to_html(), '<a href="https://example.com">Click here</a>')
    
    def test_text_to_html_node_link_missing_url(self):
        # Test handling a LINK node with missing URL
        text_node = TextNode("Broken link", TextType.LINK, None)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Broken link")
        # Verify that a missing URL is handled gracefully
        self.assertEqual(html_node.props, {"href": "#"})
        self.assertEqual(html_node.to_html(), '<a href="#">Broken link</a>')
    
    def test_text_to_html_node_image(self):
        # Test converting an IMAGE node
        text_node = TextNode("Image description", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "Image description"})
        # The HTML output should contain both attributes
        html = html_node.to_html()
        self.assertIn('alt="Image description"', html)
        self.assertIn('src="https://example.com/image.png"', html)
    
    def test_text_to_html_node_image_missing_url(self):
        # Test handling an IMAGE node with missing URL
        text_node = TextNode("Missing image", TextType.IMAGE, None)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        # Verify that a missing URL is handled gracefully
        self.assertEqual(html_node.props, {"src": "#", "alt": "Missing image"})
        self.assertIn('alt="Missing image"', html_node.to_html())
        self.assertIn('src="#"', html_node.to_html())
    
    def test_text_to_html_node_empty_text(self):
        # Test converting a node with empty text
        text_node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.to_html(), "<b></b>")

if __name__ == "__main__":
    unittest.main()