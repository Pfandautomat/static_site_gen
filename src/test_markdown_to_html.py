import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from textnode import TextNode, TextType

# Import the functions we're testing
from markdown_to_html import text_to_children, handle_code_block, create_block_node,  markdown_to_html_node


class TestMarkdownParser(unittest.TestCase):
    
    def test_text_to_children(self):
        """Test conversion of text with inline markdown to HTML nodes"""
        # Test with bold text
        children = text_to_children("This is **bold** text")
        self.assertEqual(len(children), 3)
        self.assertEqual(children[0].value, "This is ")
        self.assertEqual(children[1].tag, "b")
        self.assertEqual(children[1].value, "bold")
        self.assertEqual(children[2].value, " text")
        
        # Test with link
        children = text_to_children("Here's a [link](https://example.com)")
        self.assertEqual(len(children), 2)
        self.assertEqual(children[0].value, "Here's a ")
        self.assertEqual(children[1].tag, "a")
        self.assertEqual(children[1].value, "link")
        self.assertEqual(children[1].props["href"], "https://example.com")
    
    def test_handle_code_block(self):
        """Test handling of code blocks"""
        # Test basic code block
        code_block = "```\ndef example():\n    return True\n```"
        html_node = handle_code_block(code_block)
        
        self.assertEqual(html_node.tag, "pre")
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "code")
        self.assertEqual(html_node.children[0].value, "def example():\n    return True")
        
        # Test with language specified
        code_block = "```python\ndef example():\n    return True\n```"
        html_node = handle_code_block(code_block)
        
        self.assertEqual(html_node.tag, "pre")
        self.assertEqual(html_node.children[0].value, "def example():\n    return True")
    
    def test_create_block_node_paragraph(self):
        """Test creation of paragraph nodes"""
        block = "This is a paragraph with **bold** and _italic_ text."
        block_type = BlockType.PARAGRAPH
        
        html_node = create_block_node(block, block_type)
        
        self.assertEqual(html_node.tag, "p")
        self.assertGreater(len(html_node.children), 1)  # Should have multiple children for formatting
        
        # Verify HTML output contains formatting
        html = html_node.to_html()
        self.assertIn("<p>", html)
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("</p>", html)
    
    def test_create_block_node_heading(self):
        """Test creation of heading nodes"""
        block = "## This is a heading"
        block_type = BlockType.HEADING
        
        html_node = create_block_node(block, block_type)
        
        self.assertEqual(html_node.tag, "h2")
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].value, "This is a heading")
        
        # Verify HTML output
        html = html_node.to_html()
        self.assertEqual(html, "<h2>This is a heading</h2>")
    
    def test_create_block_node_unordered_list(self):
        """Test creation of unordered list nodes"""
        block = "- Item 1\n- Item 2\n- Item 3"
        block_type = BlockType.UNORDERED_LIST
        
        html_node = create_block_node(block, block_type)
        
        self.assertEqual(html_node.tag, "ul")
        self.assertEqual(len(html_node.children), 3)
        self.assertEqual(html_node.children[0].tag, "li")
        self.assertEqual(html_node.children[0].children[0].value, "Item 1")
        
        # Verify HTML output
        html = html_node.to_html()
        self.assertIn("<ul>", html)
        self.assertIn("<li>Item 1</li>", html)
        self.assertIn("<li>Item 2</li>", html)
        self.assertIn("<li>Item 3</li>", html)
        self.assertIn("</ul>", html)
    
    def test_create_block_node_ordered_list(self):
        """Test creation of ordered list nodes"""
        block = "1. First item\n2. Second item\n3. Third item"
        block_type = BlockType.ORDERED_LIST
        
        html_node = create_block_node(block, block_type)
        
        self.assertEqual(html_node.tag, "ol")
        self.assertEqual(len(html_node.children), 3)
        self.assertEqual(html_node.children[0].tag, "li")
        
        # Verify HTML output
        html = html_node.to_html()
        self.assertIn("<ol>", html)
        self.assertIn("<li>First item</li>", html)
        self.assertIn("<li>Second item</li>", html)
        self.assertIn("<li>Third item</li>", html)
        self.assertIn("</ol>", html)
    
    def test_create_block_node_quote(self):
        """Test creation of blockquote nodes"""
        block = "> This is a quote\n> with multiple lines"
        block_type = BlockType.QUOTE
        
        html_node = create_block_node(block, block_type)
        
        self.assertEqual(html_node.tag, "blockquote")
        
        # Verify HTML output
        html = html_node.to_html()
        self.assertIn("<blockquote>", html)
        self.assertIn("This is a quote with multiple lines", html)
        self.assertIn("</blockquote>", html)
    

if __name__ == "__main__":
    unittest.main()