import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_base(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
            ]
        
        self.assertEqual(expected, new_nodes)

    def test_bold(self):
        
        node = TextNode("This is text with a *bold text* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" word", TextType.NORMAL)
            ]
        
        self.assertEqual(expected, new_nodes)

    def test_entire_line_delimited(self):
        
        node = TextNode("*This is text with a bold text word*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        expected = [
            TextNode("This is text with a bold text word", TextType.BOLD)
            ]
        
        self.assertEqual(expected, new_nodes)
