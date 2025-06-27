import unittest
from leafnode import LeafNode

class TestHTMLLeaf(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_img(self):
        test_props = { "href": "https://www.google.com", "target": "_blank", }
        node = LeafNode(tag="img", value="this is the value", props=test_props)

        self.assertEqual(node.to_html(), "<img href=\"https://www.google.com\" target=\"_blank\">this is the value</img>")

