import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLParent(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node, child_node, child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child</span><span>child</span></div>")

    def test_to_html_with__children_and_parents(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [parent_node, parent_node, parent_node])
        self.assertEqual(parent_node2.to_html(), "<div><div><span>child</span></div><div><span>child</span></div><div><span>child</span></div></div>")

