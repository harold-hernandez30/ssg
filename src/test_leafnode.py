import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        
        node = LeafNode('p', 'Hello, paragraph')
        self.assertEqual("<p>Hello, paragraph</p>", node.to_html())

        node_props = LeafNode('h1', 'Heading', { "class":"someHeading", "data-custom":"custom-val"})
        self.assertEqual("""<h1 class="someHeading" data-custom="custom-val">Heading</h1>""", node_props.to_html())

    def test_no_tag(self):
        node = LeafNode(None, "Hello value only")
        self.assertEqual("Hello value only", node.to_html())

        node2 = LeafNode('', "Hello value only")
        self.assertEqual("Hello value only", node2.to_html())

    def test_no_value(self):
        try:
            LeafNode('p').to_html()
        except:
            self.assertRaises(expected_exception=ValueError)