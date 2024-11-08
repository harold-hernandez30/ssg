import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_html_node(self):
        node = HTMLNode('a', '', "link", { "href": "http://google.com", "target":"_blank"})
        self.assertEqual('href="http://google.com" target="_blank"', node.props_to_html())

    def test_impl_to_html(self):
        class AnchorHtmlNodeImpl(HTMLNode):
            def __init__(self, tag=None, value=None, children=None, props=None):
                super().__init__(tag, value, children, props)
            
            def to_html(self):
                return "some html impl"
        
        
        res = AnchorHtmlNodeImpl()
        html = res.to_html()
        self.assertEqual("some html impl", html)


    def test_not_impl(self):
        class AnchorHtmlNode(HTMLNode):
            def __init__(self, tag=None, value=None, children=None, props=None):
                super().__init__(tag, value, children, props)

        try: 
            res = AnchorHtmlNode().to_html()
            print(f"No exception here")
            self.assertEqual("Foo")
        except NotImplementedError:
            self.assertRaisesRegex(expected_exception=NotImplementedError, expected_regex="")






if __name__ == "__main__":
    unittest.main()