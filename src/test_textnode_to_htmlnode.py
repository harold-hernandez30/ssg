import unittest

from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal(self):
        leaf_node = text_node_to_html_node(TextNode("Hello, world", TextType.NORMAL))
        self.assertEqual("Hello, world", leaf_node.to_html())

    
    def test_bold(self):
        leaf_node = text_node_to_html_node(TextNode("Hello, world", TextType.BOLD))
        self.assertEqual("<b>Hello, world</b>", leaf_node.to_html())
    
    def test_italic(self):
        leaf_node = text_node_to_html_node(TextNode("Hello, world", TextType.ITALIC))
        self.assertEqual("<i>Hello, world</i>", leaf_node.to_html())
    
    def test_code(self):
        leaf_node = text_node_to_html_node(TextNode("Hello, world", TextType.CODE))
        self.assertEqual("<code>Hello, world</code>", leaf_node.to_html())
    
    def test_img(self):
        leaf_node = text_node_to_html_node(TextNode("Some Image", TextType.IMAGES, "http://google.com"))
        self.assertEqual("""<img src="http://google.com" alt="Some Image">""", leaf_node.to_html())
    
    def test_anchor(self):
        leaf_node = text_node_to_html_node(TextNode("Some Text", TextType.LINKS, "http://google.com"))
        self.assertEqual("""<a href="http://google.com">Some Text</a>""", leaf_node.to_html())

    def test_unsupported_text_typ(self):
        try:
            text_node_to_html_node(TextNode("Some Text", "SomeTextTYpe"))
            print("this should not print")
        except:
            print("Expecting exception")
            self.assertRaises(Exception)
