from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

from textnode import TextNode, TextType

def text_to_textnode(text):
    
    nodes = [TextNode(text, TextType.NORMAL)]

    image_nodes = split_nodes_image(nodes)
    bold_nodes = split_nodes_delimiter(image_nodes, '**', TextType.BOLD)
    italic_nodes_underscore = split_nodes_delimiter(bold_nodes, '_', TextType.ITALIC)
    italic_nodes_asterisk = split_nodes_delimiter(italic_nodes_underscore, '*', TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes_asterisk, '`', TextType.CODE)
    all_nodes = split_nodes_link(code_nodes)

    return all_nodes