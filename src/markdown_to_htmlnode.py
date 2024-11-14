from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from blocknode import BlockNode

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        nodes.append(BlockNode(block).to_htmlnode())

    return ParentNode('div', nodes)