import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode


class TestParentNode(unittest.TestCase):
    def test_leaf_nodes(self):
        parent_node = ParentNode("div",  [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"href": "http://google.com", "target": "_blank"})
        self.assertEqual(
            """<div href="http://google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>""", 
            parent_node.to_html()
            )
        
    def test_parent_node_no_props(self):
        parent_node = ParentNode("div",  [
            LeafNode("b", "Bold text")
        ])
        self.assertEqual("""<div><b>Bold text</b></div>""", parent_node.to_html())

        
    def test_parent_node_children(self):
        nested_node = ParentNode("div", [
            LeafNode(None, "Normal text")
        ])

        node = ParentNode("div", [
            LeafNode("b", "Bold text"),
            nested_node
            ]
            )
        self.assertEqual("""<div><b>Bold text</b><div>Normal text</div></div>""", node.to_html())

    def test_no_children_exception(self):
        node = ParentNode('div', None)

        try: 
            node.to_html()
        except ValueError:
            self.assertRaises(ValueError)


    def test_no_tag_exception(self):
        node = ParentNode(None, None)

        try:
            node.to_html()
        except:
            self.assertRaises(ValueError)