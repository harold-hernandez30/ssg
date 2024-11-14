import re
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
from textnode_to_htmlnode import text_node_to_html_node


def block_quote(block):
    text_nodes = text_to_textnode(block.replace('>', '').strip())
    return ParentNode('blockquote', list(map(text_node_to_html_node, text_nodes)))

def block_heading(block):
    text_nodes = text_to_textnode(block.replace('#', '').strip())
    return ParentNode(f"h{block.count('#')}", list(map(text_node_to_html_node, text_nodes)))

def block_paragraph(block):
    text_nodes = text_to_textnode(block)
    return ParentNode('p', list(map(text_node_to_html_node, text_nodes)))

def block_code(block):
    text_nodes = text_to_textnode(block.replace('```', '').strip())
    def convert_to_normal_text_node(node):
        return LeafNode(None, node.text)
    
    child_nodes =  list(map(convert_to_normal_text_node, text_nodes))

    parent_code_node = ParentNode("code", child_nodes)
    return ParentNode("pre", 
                        [
                          parent_code_node
                        ]
                      )

def block_list_item(item):
    text_nodes = text_to_textnode(item)
    return ParentNode('li', list(map(text_node_to_html_node, text_nodes)))

def block_unordered(block):

    delimiter = '-'
    if block.startswith('*'):
        delimiter = '*'

    def remove_empty_item(list_item):
        return bool(list_item)
    
    def strip_item(list_item):
        return list_item.strip()

    children_nodes = list(map(block_list_item, 
        filter(
            remove_empty_item, 
            map(strip_item, block.split(delimiter))
            )
        ))
    
    return ParentNode("ul", children_nodes)


def block_ordered(block):
    orderd_list = re.findall(r"\d\.\s.+", block)
    unnumbered_list = list(map(lambda item: re.split(r"\d\.\s", item)[1], orderd_list))
    children = map(block_list_item, unnumbered_list)
    return ParentNode('ol', children)

