from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "normal text"
    HEADING = "# Heading"
    CODE = "``` Code text ```"
    QUOTE = "> Quotes"
    UNORDERED_LIST = "- Unordered List"
    ORDERED_LIST = "1. Ordered List"


def block_to_block_type(block):

    if block =="":
        raise IndexError

    if block[0] == "#":
        return BlockType.HEADING
    
        # Check for code block
    if block.startswith("```"):
        return BlockType.CODE
    
    if block[0] == ">":
        return BlockType.QUOTE
    
    if block[0] in ["-", "*", "+"]:
        return BlockType.UNORDERED_LIST
    
    
    if block[0].isdigit():
        i = 1 
        while i < len(block) and block[i].isdigit():
            i +=1
        
        if i < len(block) and block[i] ==".":
            return BlockType.ORDERED_LIST
        
        
    return BlockType.PARAGRAPH
    


