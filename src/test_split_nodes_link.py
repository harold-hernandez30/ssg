import unittest

from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link


class TestSplitNodeLink(unittest.TestCase):
    def test_base(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). Tada!",
            TextType.NORMAL
            )
        
        new_nodes = split_nodes_link([node])
        
        self.assertEqual([
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(". Tada!", TextType.NORMAL),
        ], new_nodes)

    def test_link(self):
        node = TextNode("[Back Home](/)", TextType.NORMAL)

        new_nodes = split_nodes_link([node])      
        self.assertEqual([
            TextNode(
                "Back Home", TextType.LINK, "/"
            )
        ], new_nodes)