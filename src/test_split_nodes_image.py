import unittest

from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image


class TestSplitNodeImage(unittest.TestCase):
    def test_base(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and another image ![to youtube](https://www.youtube.com/@bootdotdev). The end",
            TextType.NORMAL
            )
        
        new_nodes = split_nodes_image([node])
        
        self.assertEqual([
            TextNode("This is text with an image ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and another image ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(". The end", TextType.NORMAL)
        ], new_nodes)