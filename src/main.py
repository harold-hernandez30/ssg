from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    print("Hello")
    node = TextNode("This is the text", TextType.BOLD, "http://google.com")
    print(f"node: {node}")
    html_node = HTMLNode("a", "another val", "hello", {"href": "http://google.com", "target": "_blank"})
    print(f"html node: {html_node}")
    print(f"props: {html_node.props_to_html()}")
    leaf_node = LeafNode("a", "some val", {"href": "http://google.com", "target": "_blank"})
    print(f"leaf_node: {leaf_node.props_to_html()}")
    print(f"leaf_node: {leaf_node.__repr__()}")
    parent_node = ParentNode("div",  [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], {"href": "http://google.com", "target": "_blank"})
    print(f"parent_node: {parent_node.to_html()}")



main()