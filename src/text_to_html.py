from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            url = text_node.url if text_node.url is not None else "#"
            return LeafNode("a", text_node.text, props={"href": url})
        
        case TextType.IMAGE:
            url = text_node.url if text_node.url is not None else "#"
            return LeafNode("img", "", props={"src": url, "alt":text_node.text})
            
        







