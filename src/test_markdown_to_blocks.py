import unittest

from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from medialeafnode import MediaLeafNode
from parentnode import ParentNode

class TestMarkdownToBlock(unittest.TestCase):
    def test_base(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(expected, markdown_to_blocks(markdown))