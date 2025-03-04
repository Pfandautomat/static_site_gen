import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode(tag="span", children=[grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_with_single_leaf_child(self):
        # Create a parent with a single leaf child
        leaf = LeafNode("p", "Hello, world!")
        parent = ParentNode(tag="div", children=[leaf])
        
        # Check the output HTML
        expected = "<div><p>Hello, world!</p></div>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_node_with_multiple_leaf_children(self):
        # Create a parent with multiple leaf children
        item1 = LeafNode("li", "Item 1")
        item2 = LeafNode("li", "Item 2")
        item3 = LeafNode("li", "Item 3")
        
        parent = ParentNode(tag="ul", children=[item1, item2, item3])
        
        # Check the output HTML
        expected = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_node_with_props(self):
        # Test parent node with HTML attributes
        leaf = LeafNode("p", "Content")
        parent = ParentNode(
            tag="div", 
            children=[leaf], 
            props={"class": "container", "id": "main"}
        )
        
        # The actual output order of attributes might vary
        html = parent.to_html()
        self.assertIn('<div', html)
        self.assertIn('class="container"', html)
        self.assertIn('id="main"', html)
        self.assertIn('<p>Content</p>', html)
        self.assertIn('</div>', html)
    
    def test_nested_parent_nodes(self):
        # Create a nested structure
        inner_text = LeafNode("p", "Inner text")
        inner_parent = ParentNode(tag="div", children=[inner_text], props={"class": "inner"})
        outer_parent = ParentNode(tag="div", children=[inner_parent], props={"class": "outer"})
        
        expected = '<div class="outer"><div class="inner"><p>Inner text</p></div></div>'
        self.assertEqual(outer_parent.to_html(), expected)
    
    def test_parent_node_with_no_children(self):
        # Test error handling for no children
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None)
    
    # NOTE: If your implementation doesn't check for empty lists, 
    # you might need to remove this test or modify your implementation
    def test_parent_node_with_empty_children_list(self):
        # Test error handling for empty children list
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[])
    
    def test_parent_node_with_no_tag(self):
        # Test error handling for no tag
        leaf = LeafNode("p", "Content")
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[leaf])
    
    def test_mixed_node_types(self):
        # Test with both text nodes and leaf nodes as children
        text_node = LeafNode(value="Plain text")
        element_node = LeafNode("span", "Styled text")
        
        parent = ParentNode(tag="div", children=[text_node, element_node])
        
        expected = "<div>Plain text<span>Styled text</span></div>"
        self.assertEqual(parent.to_html(), expected)
    
if __name__== "__main__":
    unittest.main()