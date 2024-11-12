import re

def block_to_block_type(block):
    block_type = "paragraph"

    if is_code(block):
        block_type = "code"

    if is_heading(block):
        block_type = "heading"

    if is_quote(block):
        block_type = "quote"

    if is_ordered(block):
        block_type = "ordered"

    if is_unorderd(block):
        block_type = "unordered"

    return block_type

def is_code(block):
    return len(re.findall(r"^`{3}(.*?)`{3}$", block)) > 0

def is_heading(block):
    # FIXME: should exactly have one space between # and "heading text"
    return len(re.findall(r"^#{1,6}\s{1}(.*?)$", block)) > 0

def is_quote(block):
    return len(re.findall(r"^>{1}\s.+$", block)) > 0

def is_unorderd(block):
    return len(re.findall(r"^[\*|-]{1}\s.+(\n\s[\*|-]{1}\s.+)?", block)) > 0

def is_ordered(block):
    return len(re.findall(r"^(\d\.\s).+(\n\s\d\.\s.+)*", block)) > 0
