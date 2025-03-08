from textnode import *


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


                
            



