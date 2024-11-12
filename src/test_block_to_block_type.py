import unittest

from block_to_block_type import block_to_block_type, is_code, is_heading, is_ordered, is_quote, is_unorderd

class TestBlockToBlockType(unittest.TestCase):
    # def test_base(self):
    #     expected = []
    #     result = block_to_block_type("")
    #     self.assertEqual(expected, result)

    def test_paragraph(self):
        normal_paragraph = "this is a paragraph"
        multi_line_paragraph = "line 1 of paragraph\n line 2 of paragraph"
        self.assertEqual("paragraph", block_to_block_type(normal_paragraph))
        self.assertEqual("paragraph", block_to_block_type(multi_line_paragraph))

    def test_code(self):
        code_block = "``` this is your code ```"
        self.assertEqual("code", block_to_block_type(code_block))

    def test_heading(self):
        not_a_heading = "not a heading"
        heading1 = "# some heading 1"
        heading2 = "## some heading 2"
        heading3 = "### some heading 3"
        heading4 = "#### some heading 4"
        heading5 = "##### some heading 5"
        heading6 = "###### some heading 6"
        heading_7_more = "####### some heading n"
        self.assertEqual("heading", block_to_block_type(heading1))
        self.assertEqual("heading", block_to_block_type(heading2))
        self.assertEqual("heading", block_to_block_type(heading3))
        self.assertEqual("heading", block_to_block_type(heading4))
        self.assertEqual("heading", block_to_block_type(heading5))
        self.assertEqual("heading", block_to_block_type(heading6))
        self.assertEqual("paragraph", block_to_block_type(heading_7_more))
        self.assertEqual("paragraph", block_to_block_type(not_a_heading))


    def test_quote(self):
        quote_text = "> this is a quote"
        not_a_quote = "this is not a quote"
        self.assertEqual("quote", block_to_block_type(quote_text))
        self.assertEqual("paragraph", block_to_block_type(not_a_quote))

    def test_unordered_list(self):
        unordered_list_hyphen = "- Item 1\n - Item 2\n - Item 3"
        unordered_list_asterisk = "* Item 1\n * Item 2\n * Item 3"
        self.assertEqual("unordered", block_to_block_type(unordered_list_hyphen))
        self.assertEqual("unordered", block_to_block_type(unordered_list_asterisk))

    def test_ordered_list(self):
        ordered_list = "1. Item 1\n 2. Item 2\n 3. Item 3"
        self.assertEqual("ordered", block_to_block_type(ordered_list))

    # Helper function tests

    def test_helpers_code(self):
        self.assertEqual(True, is_code("``` this is a code ```"))
        self.assertEqual(True, is_code("```this is a code```"))
        self.assertEqual(False, is_code("```this is not a code"))

    def test_helpers_heading(self):
        self.assertEqual(True, is_heading("# heading 1"))
        self.assertEqual(False, is_heading("#heading 1"))
        self.assertEqual(True, is_heading("#  heading 1"))
        self.assertEqual(True, is_heading("## heading 2"))
        self.assertEqual(True, is_heading("###### heading 6"))
        self.assertEqual(False, is_heading("####### heading 6 + 1"))

    def test_helpers_quote(self):
        self.assertEqual(True, is_quote("> your quote"))
        self.assertEqual(True, is_quote(">  your quote"))
        self.assertEqual(False, is_quote(">not a valid quote"))
        self.assertEqual(False, is_quote(">> not a valid quote"))

    def test_helpers_ordered(self):
        self.assertEqual(True, is_ordered("1. Item 1"))
        self.assertEqual(False, is_ordered("1.Item 1"))
        self.assertEqual(False, is_ordered("X.Item X"))
        self.assertEqual(True, is_ordered("1. Item X\n 2. Item 2"))

    
    def test_helpers_unordered(self):
        self.assertEqual(True, is_unorderd("- Valid 1"))
        self.assertEqual(False, is_unorderd("-- Not a valid item 1"))
        self.assertEqual(False, is_unorderd("-Not valid item 1"))
        self.assertEqual(True, is_unorderd("* Valid Item 1"))
        self.assertEqual(False, is_unorderd("** Not a valid Item 1"))
        self.assertEqual(False, is_unorderd("*Not valid"))




