from textnode import *
from extracts_funcs import extract_markdown_images, extract_markdown_links
import re 


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT :
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) == 1:
            new_nodes.append(node)
            continue

        for i in range (0,len(parts)-1,2):
            if parts[i]:
                new_nodes.append(TextNode(parts[i],TextType.TEXT))

            if  len(parts) > i+1 and parts[i+1]:
                new_nodes.append(TextNode(parts[i+1],text_type))    
            
        if len(parts) % 2 == 1 and parts[-1]:
              new_nodes.append(TextNode(parts[-1],TextType.TEXT))


    return new_nodes


                
def split_nodes_image(old_nodes):

    new_nodes = []


    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        extracts = extract_markdown_images(original_text)

        if len(extracts) < 1:
            new_nodes.append(node)
            continue

        for extract in extracts:

            sections =  original_text.split(f"![{extract[0]}]({extract[1]})", 1)
            
            if len(sections) != 2:
                raise ValueError
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            
            new_nodes.append(TextNode(extract[0],TextType.IMAGE,extract[1]))

            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT))

    return new_nodes





def split_nodes_link(old_nodes):
    
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        extracts = extract_markdown_links(original_text)

        # Check if only text note without links
        if len(extracts) < 1:
            new_nodes.append(node)
            continue
        
        for extract in extracts:

            sections = original_text.split(f"[{extract[0]}]({extract[1]})", 1)

            if len(sections) !=  2:
                raise ValueError
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            
            new_nodes.append(TextNode(extract[0],TextType.LINK,extract[1]))

            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes
