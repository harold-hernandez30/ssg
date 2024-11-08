from textnode import TextNode
from textnode import TextType

def main():
    print("Hello")
    node = TextNode("This is the text", TextType.BOLD, "http://google.com")
    print(f"node: {node}")


main()