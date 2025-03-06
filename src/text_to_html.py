from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)





