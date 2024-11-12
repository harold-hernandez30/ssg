from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

from textnode import TextNode, TextType

def text_to_textnode(text):
    
    nodes = [TextNode(text, TextType.NORMAL)]
    print(f"DEBUG: original nodes: {nodes}\n")
    # print(f"DEBUG: image nodes: {split_nodes_image(nodes)}\n")
    # print(f"DEBUG: bold nodes: {split_nodes_delimiter(nodes, '**', TextType.BOLD)}\n")
    # print(f"DEBUG: italic nodes: {split_nodes_delimiter(nodes, '*', TextType.ITALIC)}\n")
    # print(f"DEBUG: code nodes: {split_nodes_delimiter(nodes, '`', TextType.CODE)}\n")
    # print(f"DEBUG: link nodes: {split_nodes_link(nodes)}\n")

    image_nodes = split_nodes_image(nodes)
    print(f"DEBUG: image_nodes: {image_nodes}")
    bold_nodes = split_nodes_delimiter(image_nodes, '**', TextType.BOLD)
    print(f"DEBUG: bold_nodes: {bold_nodes}")

    italic_nodes = split_nodes_delimiter(bold_nodes, '*', TextType.ITALIC)
    print(f"DEBUG: italic_nodes: {italic_nodes}")

    code_nodes = split_nodes_delimiter(italic_nodes, '`', TextType.CODE)
    print(f"DEBUG: code_nodes: {code_nodes}")

    all_nodes = split_nodes_link(code_nodes)
    print(f"DEBUG: all_nodes: {all_nodes}")

    return all_nodes

    # return split_nodes_delimiter(
    #     split_nodes_delimiter(
    #         split_nodes_delimiter(
    #             split_nodes_link(
    #                 split_nodes_image(nodes)
    #                 ),
    #                   '`', TextType.CODE), 
    #                   '**', TextType.BOLD), 
    #                   "*", TextType.ITALIC)