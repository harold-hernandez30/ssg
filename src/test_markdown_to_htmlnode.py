import unittest

from markdown_to_htmlnode import markdown_to_htmlnode
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from parentnode import ParentNode
from textnode_to_htmlnode import text_node_to_html_node

class TestMarkDownToHTMLNode(unittest.TestCase):
    def test_base(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
"""
        result = markdown_to_htmlnode(markdown).to_html()
        expected = ParentNode("div", [
            ParentNode("h1", [text_node_to_html_node(TextNode("This is a heading", TextType.NORMAL))]),
            ParentNode("p", [
                text_node_to_html_node(TextNode("This is a paragraph of text. It has some ", TextType.NORMAL)),
                text_node_to_html_node(TextNode("bold", TextType.BOLD)),
                text_node_to_html_node(TextNode(" and ", TextType.NORMAL)),
                text_node_to_html_node(TextNode("italic", TextType.ITALIC)),
                text_node_to_html_node(TextNode(" words inside of it.", TextType.NORMAL)),
            ]),
            ParentNode("ul", [
                ParentNode("li", [ text_node_to_html_node(TextNode("This is the first list item in a list block", TextType.NORMAL))])
            ]),
            
        ]).to_html()
        self.assertEqual(expected, result)