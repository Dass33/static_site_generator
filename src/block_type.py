from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


import re

def block_to_block_type(block: str) -> BlockType:
    if re.fullmatch( r"#{1,6}[^#]?.*",block) != None:
        return BlockType.HEADING
    if re.fullmatch(r"^```.*```$", block, re.DOTALL) != None:
        return BlockType.CODE

    all_quotes = True
    all_unordered_list = True
    all_ordered_list = True
        
    for line in block.split('\n'):
        if re.fullmatch(r"^>.*", line) == None:
            all_quotes = False
        if re.fullmatch(r"^- .*", line) == None:
            all_unordered_list = False
        if re.fullmatch(r"^\d+\. .*", line) == None:
            all_ordered_list = False


    if all_quotes:
        return BlockType.QUOTE
    if all_unordered_list:
        return BlockType.UNORDERED_LIST
    if all_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
