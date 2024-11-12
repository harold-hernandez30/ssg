from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        text_remaining = node.text
        markdown_links = extract_markdown_links(node.text)
    

        for i in range(len(markdown_links)):
            markdown_link = markdown_links[i]
            text, url = markdown_link
            text_arr =  text_remaining.split(f"[{text}]({url})", 1)
            text_left_hand = text_arr[0]
            text_remaining = text_arr[1]
            new_nodes.append(TextNode(text_left_hand, TextType.NORMAL))
            new_nodes.append(TextNode(text, TextType.LINK, url))

            if i == len(markdown_links) - 1 and text_remaining:
                new_nodes.append(TextNode(text_remaining, TextType.NORMAL))
                
    return new_nodes