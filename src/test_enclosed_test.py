import unittest

from enclosed_text import enclosed_text


class TestSplitNode(unittest.TestCase):
    def test_indices(self):
        self.assertEqual("code block", enclosed_text("This is text with a `code block` word", '`'))
        
        self.assertEqual("bold text", enclosed_text("This is text with a **bold text** word", '**'))
        self.assertEqual("All bold text", enclosed_text("*All bold text*", '*'))