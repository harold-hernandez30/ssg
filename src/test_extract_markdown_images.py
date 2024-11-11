import unittest

from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):

    def test_base(self): 
        text =  "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        result = extract_markdown_images(text)

        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(expected, result)

    