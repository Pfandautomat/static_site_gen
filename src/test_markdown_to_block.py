import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_single_paragraph(self):
        # Test with a single paragraph
        markdown = "This is a simple paragraph."
        expected = ["This is a simple paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_multiple_paragraphs(self):
        # Test with multiple paragraphs separated by blank lines
        markdown = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        expected = ["First paragraph.", "Second paragraph.", "Third paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_headers(self):
        # Test with different header levels
        markdown = "# Header 1\n\n## Header 2\n\n### Header 3"
        expected = ["# Header 1", "## Header 2", "### Header 3"]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_mixed_content(self):
        # Test with mixed content (paragraphs and headers)
        markdown = "# Header\n\nThis is a paragraph.\n\n## Subheader\n\nAnother paragraph."
        expected = ["# Header", "This is a paragraph.", "## Subheader", "Another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_lists(self):
        # Test with unordered and ordered lists
        markdown = "- Item 1\n- Item 2\n- Item 3\n\n1. First\n2. Second\n3. Third"
        expected = ["- Item 1\n- Item 2\n- Item 3", "1. First\n2. Second\n3. Third"]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_code_blocks(self):
        # Test with code blocks using triple backticks
        markdown = "Regular text.\n\n```python\ndef function():\n    pass\n```\n\nMore text."
        expected = ["Regular text.", "```python\ndef function():\n    pass\n```", "More text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_blockquotes(self):
        # Test with blockquotes
        markdown = "Normal text.\n\n> This is a quote.\n> It spans multiple lines.\n\nMore text."
        expected = ["Normal text.", "> This is a quote.\n> It spans multiple lines.", "More text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_empty_input(self):
        # Test with empty input
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_whitespace_only(self):
        # Test with whitespace only
        markdown = "   \n\n   \n  "
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_trailing_newlines(self):
        # Test with trailing newlines
        markdown = "Paragraph.\n\n"
        expected = ["Paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()