import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_base(self):

        input = "# Title"
        expected = "Title"
        self.assertEqual(expected, extract_title(input))

    def test_no_title(self):

        input = "Title"
        try:
            extract_title(input)
        except:
            print("Exception raised")
            self.assertRaises(expected_exception=Exception)