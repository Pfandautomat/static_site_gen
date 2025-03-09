from split_nodes_delimiter import *


def text_to_textnodes(text):
    
    nodes = [TextNode(text,TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Italic text: _text_
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Code: `text`
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    return nodes
