from block_types import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


def text_to_children(text):

    

    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)

    return html_nodes


def handle_code_block(block):
    
    lines = block.split("\n")

    if len(lines) > 2:
        # Check if first line has language specification
        if lines[0].startswith("```"):
            # Skip the first line with ``` and the last line with ```
            code_content = "\n".join(lines[1:-1])
        else:
            code_content = "\n".join(lines)
    
    else:
        code_content = block.strip("```").strip()

    text_node = TextNode(code_content,TextType.CODE)

    code_node = text_node_to_html_node(text_node)

    return ParentNode("pre",children=[code_node])


def create_block_node(block, block_type):
    """
    Create an HTML node for a specific block type.
    
    Args:
        block (str): The markdown block content
        block_type (BlockType): The type of the block
        
    Returns:
        HTMLNode: An appropriate HTML node for the block
    """
    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(block)
        return ParentNode("p", children=children)
    
    elif block_type == BlockType.HEADING:
        # Count the number of # to determine heading level
        level = 0
        for char in block:
            if char == '#':
                level += 1
            else:
                break
        
        # Get the heading text without # symbols
        heading_text = block[level:].strip()
        children = text_to_children(heading_text)
        return ParentNode(f"h{level}", children=children)
    
    elif block_type == BlockType.QUOTE:
        # Remove the '>' prefix from each line
        quote_text = ""
        for line in block.split("\n"):
            if line.startswith(">"):
                quote_text += line[1:].strip() + " "
            else:
                quote_text += line.strip() + " "
        
        children = text_to_children(quote_text.strip())
        return ParentNode("blockquote", children=children)
    
    elif block_type == BlockType.UNORDERED_LIST:
        # Process each list item
        items = []
        for line in block.split("\n"):
            if line.strip():
                # Remove list marker (-, *, +) and get item text
                item_text = line.strip()
                if item_text[0] in ['-', '*', '+']:
                    item_text = item_text[1:].strip()
                    
                item_children = text_to_children(item_text)
                items.append(ParentNode("li", children=item_children))
        
        return ParentNode("ul", children=items)
    
    elif block_type == BlockType.ORDERED_LIST:
        # Process each numbered list item
        items = []
        for line in block.split("\n"):
            if line.strip():
                # Find the period after the number
                for i, char in enumerate(line):
                    if char == '.' and i > 0:
                        item_text = line[i+1:].strip()
                        item_children = text_to_children(item_text)
                        items.append(ParentNode("li", children=item_children))
                        break
        
        return ParentNode("ol", children=items)
    
    # Default case - should not normally be reached
    return ParentNode("div", children=text_to_children(block))




def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)


    blocks = markdown_to_blocks(markdown)
    
    # Process each block into HTML nodes
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        # Handle different block types
        if block_type == BlockType.CODE:
            html_node = handle_code_block(block)
        else:
            # Handle all other block types based on their specific needs
            html_node = create_block_node(block, block_type)
        
        html_nodes.append(html_node)
    
    # Combine all block nodes under a parent div
    return ParentNode("div", children=html_nodes)