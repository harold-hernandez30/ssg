from textnode import TextNode
from textnode import TextType

def main():
    print("Hello")
    node = TextNode("This is the text", TextType.HTML, "http://google.com")
    print(f"node: {node}")


main()