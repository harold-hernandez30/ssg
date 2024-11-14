import unittest
from block_to_blocknode import (
    block_heading, 
    block_paragraph, 
    block_code, 
    block_quote, 
    block_unordered, 
    block_ordered
)

from parentnode import ParentNode
from leafnode import LeafNode

class TestBlockToBlockNode(unittest.TestCase):
    def test_heading(self):
        expected1 = "<h1>Title</h1>"
        self.assertEqual(expected1, block_heading("# Title").to_html())
        expected2 = ParentNode('h2', 
                               [
                                   LeafNode(None, "Title")
                                ]).to_html()
        self.assertEqual(expected2, block_heading("## Title").to_html())

        expected3 = "<h6>Title</h6>"
        self.assertEqual(expected3, block_heading("###### Title").to_html())

    def test_paragraph(self):
        expected1 = ParentNode('p',
                                [
                                    LeafNode(None, "Hello, random")
                                 ]).to_html()
        self.assertEqual(expected1, 
                         block_paragraph("Hello, random").to_html())
        
        expected2 = "<p>Hello, random</p>"
        self.assertEqual(expected2, block_paragraph("Hello, random").to_html())

        expected3 = """<p><i>My name</i> is <b>slim shady</b>. Here's my picture <img src="http://slim.com/shady.jpeg" alt="slim shady"></p>"""
        self.assertEqual(expected3, 
                         block_paragraph("*My name* is **slim shady**. Here's my picture ![slim shady](http://slim.com/shady.jpeg)").to_html())

    def test_code(self):
        expected = "<pre><code>this is code</code></pre>"
        self.assertEqual(expected, block_code("```this is code```").to_html())

        expected1 = ParentNode('pre',  [ 
                ParentNode('code', [ LeafNode(None, "this is code") ])
            ]).to_html()
        self.assertEqual(expected1, block_code("```this is code```").to_html())

        
        expected1 = ParentNode('pre',  [ 
                ParentNode('code', [ LeafNode(None, "this is code\nanother code") ])
            ]).to_html()
        self.assertEqual(expected1, block_code("```this is code\nanother code```").to_html())
        

        # FIXME: does not support multiline code
#         expected2 = ParentNode('pre', 
#                 [
#                     ParentNode('code', [LeafNode(None, "this is code"), LeafNode(None, "Another code")])
#                 ]).to_html()
#         self.assertEqual(expected2, block_code(
# """
# ```
# this is code
# Another code

# ```            
# """).to_html())
        
    def test_quote(self):

        expected1 = "<blockquote>This is a quote</blockquote>"
        result1 = block_quote("> This is a quote").to_html()
        self.assertEqual(expected1, result1)
        result = block_quote(">    This is a quote with new line and white space    \n").to_html()
        expected = ParentNode('blockquote',  [ LeafNode(None, 'This is a quote with new line and white space')]).to_html()
        self.assertEqual(expected, result)

    def test_unordered(self):
        expected1 = ParentNode('ul', [
                                        ParentNode("li", [LeafNode(None, "Item 1")]), 
                                        ParentNode("li", [LeafNode(None, "Item 2")]), 
                                        ParentNode("li", [LeafNode(None, "Item 3")]), 
                                        ]
                                    ).to_html()
                        
        self.assertEqual(expected1, block_unordered("- Item 1\n - Item 2\n - Item 3").to_html())
                         
        expected2 = ParentNode('ul', [
                                        ParentNode("li", [LeafNode(None, "Item 1")]), 
                                        ParentNode("li", [LeafNode(None, "Item 2")]), 
                                        ParentNode("li", [LeafNode(None, "Item 3")]), 
                                        ]
                                    ).to_html()
        self.assertEqual(expected2, block_unordered("* Item 1\n * Item 2\n * Item 3").to_html())

        expected3 = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(expected3, block_unordered("- Item 1\n - Item 2\n - Item 3").to_html())


    def test_ordered(self):
        expected1 = ParentNode('ol', [
                                        ParentNode("li", [LeafNode(None, "Item 1")]), 
                                        ParentNode("li", [LeafNode(None, "Item 2")]), 
                                        ParentNode("li", [LeafNode(None, "Item 3")]), 
                                        ]
                                    ).to_html()
        self.assertEqual(expected1, block_ordered("1. Item 1\n 2. Item 2\n 3. Item 3").to_html() )

        expected2 =  ParentNode('ol', [
                                        ParentNode("li", [LeafNode(None, "Item 10")]), 
                                        ParentNode("li", [LeafNode(None, "Item 11")]), 
                                        ParentNode("li", [LeafNode(None, "Item 12")]), 
                                        ]
                                    ).to_html()
        self.assertEqual(expected2, block_ordered("10. Item 10\n 11. Item 11\n 12. Item 12").to_html())
        
        expected3 = "<ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol>"
        self.assertEqual(expected3, block_ordered("1. Item 1\n 2. Item 2\n 3. Item 3").to_html())