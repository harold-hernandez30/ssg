import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertEqual(None, node.url)
        self.assertEqual(None, node2.url)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(None, node.url)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertEqual("http://google.com", node2.url)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is is also an italic node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)



if __name__ == "__main__":
    unittest.main()