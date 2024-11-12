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
        
        node = TextNode("This is text with a **bold text** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" word", TextType.NORMAL)
            ]
        
        self.assertEqual(expected, new_nodes)

    def test_entire_line_delimited(self):
        
        node = TextNode("**This is text with a bold text word**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [ TextNode("This is text with a bold text word", TextType.BOLD)]
        
        self.assertEqual(expected, new_nodes)

    
    def test_multiple_delimited_line(self):
        
        node = TextNode("**bold** `code` _you_ got there", TextType.NORMAL)
        bold_node = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual([
            TextNode("bold", TextType.BOLD),
            TextNode(" `code` _you_ got there", TextType.NORMAL)
        ], bold_node)

        
        code_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual([
            TextNode("**bold** ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" _you_ got there", TextType.NORMAL)
        ], code_node)
        
        code_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([
            TextNode("**bold** `code` ", TextType.NORMAL),
            TextNode("you", TextType.ITALIC),
            TextNode(" got there", TextType.NORMAL)
        ], code_node)

    def test_multiple_nodes(self):
        first_node = TextNode("First node **bold** word", TextType.NORMAL)
        second_node = TextNode("Second node **another bold** word", TextType.NORMAL)
        third_node = TextNode("Third node **last bold** word", TextType.NORMAL)
        result = split_nodes_delimiter([first_node, second_node, third_node], "**", TextType.BOLD)

        expected = [
            TextNode("First node ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            TextNode("Second node ", TextType.NORMAL),
            TextNode("another bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            TextNode("Third node ", TextType.NORMAL),
            TextNode("last bold", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(expected, result)