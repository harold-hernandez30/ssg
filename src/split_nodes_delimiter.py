from textnode import TextNode, TextType
from enclosed_text import enclosed_text

def assert_closing_delimiter(text, delimiter):
    if text.count(delimiter) != 2:
        raise Exception(f"No closing delimiter found for: {delimiter}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def split_node(node):
        text_arr = node.text.split(delimiter)
        target_text = enclosed_text(node.text, delimiter)

        def convert(text):
            if text == target_text:
                return TextNode(text, text_type)
            else:
                return TextNode(text, TextType.NORMAL)


        
        splitted_node_debug = list(map(convert, text_arr))
        return splitted_node_debug

    all_nodes = []
    for node in old_nodes:
        assert_closing_delimiter(node.text, delimiter)
        all_nodes.extend(split_node(node))


    
    return all_nodes