import re
from blocktype import BlockType

def block_to_block_type(block):
    block_type = BlockType.PARAGRAPH

    if is_code(block):
        block_type = BlockType.CODE

    if is_heading(block):
        block_type = BlockType.HEADING

    if is_quote(block):
        block_type = BlockType.QUOTE

    if is_ordered(block):
        block_type = BlockType.ORDERED_LIST

    if is_unorderd(block):
        block_type = BlockType.UNORDERED_LIST

    return block_type

def is_code(block):
    return len(re.findall(r"`{3}.*?`{3}", block, re.DOTALL)) > 0

def is_heading(block):
    # FIXME: should exactly have one space between # and "heading text"
    return len(re.findall(r"^#{1,6}\s{1}(.*?)$", block)) > 0

def is_quote(block):
    return len(re.findall(r"^>{1}\s.+$", block)) > 0

def is_unorderd(block):
    return len(re.findall(r"^[\*|-]{1}\s.+(\n\s[\*|-]{1}\s.+)?", block)) > 0

def is_ordered(block):
    return len(re.findall(r"^(\d\.\s).+(\n\s\d\.\s.+)*", block)) > 0
