import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode()
        node.props = {}
        self.assertEqual(node.props_to_html(), "")


    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode()
        node.props = {"class": "container"}
        self.assertEqual(node.props_to_html(), ' class="container"')
    
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode()
        node.props = {
            "href": "https://www.example.com",
            "target": "_blank",
            "rel": "noopener"
        }

    



if __name__ == "__main__":
    unittest.main()
