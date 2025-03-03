import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_node_with_tag_and_value(self):
        # Test basic leaf node with tag and value
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_leaf_node_with_tag_value_and_props(self):
        # Test leaf node with tag, value, and properties
        node = LeafNode("a", "Click me", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')
    
    def test_leaf_node_with_multiple_props(self):
        # Test leaf node with multiple properties
        node = LeafNode(
            "a", 
            "Click me", 
            props={
                "href": "https://example.com", 
                "target": "_blank", 
                "class": "button"
            }
        )
        # Note: The exact string comparison might be challenging due to prop order
        html = node.to_html()
        self.assertIn('<a ', html)
        self.assertIn('href="https://example.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertIn('class="button"', html)
        self.assertIn('>Click me</a>', html)
    
    def test_leaf_node_without_tag(self):
        # Test leaf node without a tag (just text)
        node = LeafNode(value="Plain text")
        self.assertEqual(node.to_html(), "Plain text")
    
    def test_leaf_node_with_none_value(self):
        # Test that ValueError is raised when value is None
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    
    def test_leaf_node_preserves_none_children(self):
        # Test that children is always None, even if provided
        node = LeafNode("p", "Text", children=["shouldn't be here"])
        self.assertIsNone(node.children)
    
    def test_leaf_node_with_special_characters(self):
        # Test with HTML special characters
        node = LeafNode("div", "a < b & c > d")
        # Note: This test might fail if your implementation automatically escapes HTML
        # If not, this is a good opportunity to consider HTML escaping
        self.assertEqual(node.to_html(), "<div>a < b & c > d</div>")


if __name__ == "__main__":
    unittest.main()