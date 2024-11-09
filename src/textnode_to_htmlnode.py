from textnode import TextType
from leafnode import LeafNode
from medialeafnode import MediaLeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.IMAGES:
            return MediaLeafNode('img', {"src":text_node.url, "alt": text_node.text})
        case TextType.LINKS:
            return LeafNode('a', text_node.text, {"href":text_node.url})
        case _:
            raise Exception("TextType: {text_node.type} is not supported")