import unittest
from block_types import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    
    def test_paragraph(self):
        # Test basic paragraph detection
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test heading detection at different levels
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
    
    def test_code_block(self):
        # Test code block detection
        block = "```python\ndef function():\n    pass"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_quote(self):
        # Test blockquote detection
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_unordered_list(self):
        # Test unordered list detection with different markers
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("* Item 1"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("+ Item 1"), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        # Test simple ordered list detection
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)
        
        # Test with numbers other than 1
        self.assertEqual(block_to_block_type("5. Fifth item"), BlockType.ORDERED_LIST)
        
        # Test with double-digit numbers
        self.assertEqual(block_to_block_type("10. Tenth item"), BlockType.ORDERED_LIST)
    
    def test_edge_cases(self):
        # Test with empty string
        with self.assertRaises(IndexError):
            block_to_block_type("")
        
        # Test with string that looks like number but isn't an ordered list
        block = "12 Days of Christmas"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Test with number followed by something other than period
        block = "1) First item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()