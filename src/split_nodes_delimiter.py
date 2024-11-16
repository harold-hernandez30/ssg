from textnode import TextNode, TextType
from enclosed_text import enclosed_text
import re

def assert_closing_delimiter(text, delimiter):
    pass
    # if text.count(delimiter) % 2 != 0:
    #     raise Exception(f"No closing delimiter found for: {delimiter}, count: {text.count(delimiter)}")

def escape_delimiter(delimiter):
    match delimiter:
        case '*':
            return "\*"
        case "**":
            return "\*\*"
        case _:
            return delimiter

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def split_node(node):
        text_remaining = node.text
        escaped_delimiter = escape_delimiter(delimiter)
        text_arr = list(filter(lambda item: item, re.findall(rf"{escaped_delimiter}(.*?){escaped_delimiter}", text_remaining)))

            
        new_nodes = []
        for i in range(len(text_arr)):
            text = text_arr[i]
            
            result = text_remaining.split(f"{delimiter}{text}{delimiter}", 1)

            text_left_hand = None
            if len(result) == 2:
                text_left_hand = result[0]
                text_remaining = result[1]
            else:
                text_remaining = result[0]
                
            
            if text_left_hand:
                new_nodes.append(TextNode(text_left_hand, TextType.NORMAL))

            if text:
                new_nodes.append(TextNode(text, text_type))

            if i == len(text_arr) - 1 and text_remaining:
                new_nodes.append(TextNode(text_remaining, TextType.NORMAL))
        return new_nodes

    all_nodes = []
    for node in old_nodes:
        assert_closing_delimiter(node.text, delimiter)

        result = split_node(node)
        if len(result) == 0:
            all_nodes.append(node)
        else:
            all_nodes.extend(result)
    
    return all_nodes