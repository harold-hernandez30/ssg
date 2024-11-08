from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    print("Hello")
    node = TextNode("This is the text", TextType.BOLD, "http://google.com")
    print(f"node: {node}")
    html_node = HTMLNode("a", "", "hello", {"href": "http://google.com", "target": "_blank"})
    print(f"html node: {html_node}")
    print(f"props: {html_node.props_to_html()}")
    leaf_node = LeafNode("a", "", {"href": "http://google.com", "target": "_blank"})
    print(f"leaf_node: {leaf_node.props_to_html()}")
    print(f"leaf_node: {leaf_node.__repr__()}")


main()