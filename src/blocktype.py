from enum import Enum

class BlockType(Enum):
    CODE = "code"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered"
    ORDERED_LIST = "ordered"