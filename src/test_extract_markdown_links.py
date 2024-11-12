import unittest

from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links

class TestExtractMarkDownLinks(unittest.TestCase):
    def test_base(self):
        text =  "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        result = extract_markdown_links(text)

        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(expected, result)
