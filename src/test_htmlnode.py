import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        test_props = { "href": "https://www.google.com", "target": "_blank", }
        node = HTMLNode(tag="p", value="this is the value", props=test_props)
        ref_text = "p, this is the value, None,  href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(str(node), ref_text)


    def test_eq1(self):
        node = HTMLNode()
        ref_text = "None, None, None, "

        self.assertEqual(str(node), ref_text)


    def test_eq2(self):
        node = HTMLNode(tag="h1", value="this is the value")
        ref_text = "h1, this is the value, None, "

        self.assertEqual(str(node), ref_text)

