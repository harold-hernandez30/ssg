from blocktype import BlockType
from block_to_block_type import block_to_block_type
from block_to_blocknode import (
    block_code, 
    block_heading, 
    block_ordered, 
    block_paragraph, 
    block_quote, 
    block_unordered
)


class BlockNode:
    def __init__(self, block):
        self.block = block

    def __eq__(self, other):
        return self.block == other.block 
    
    def __repr__(self):
        return self.block
    
    def to_htmlnode(self): 
        block = self.block
        block_type = block_to_block_type(block)
        
        match block_type: 
            case BlockType.HEADING:
                return block_heading(block)
            case BlockType.PARAGRAPH:
                return block_paragraph(block)
            case BlockType.QUOTE:
                return block_quote(block)
            case BlockType.CODE:
                return block_code(block)
            case BlockType.UNORDERED_LIST:
                return block_unordered(block)
            case BlockType.ORDERED_LIST:
                return block_ordered(block)
            case _:
                raise Exception(f"Invalid block type: {block_type}")
    
    def __repr__(self):
        return f"BlockNode({self.block})"
