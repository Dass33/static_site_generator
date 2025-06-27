from extract_title import extract_title
from markdown_to_html import markdown_to_html_node
import unittest

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_list(self):
        md = """
- This is text that _should_ remain
- the **same** even with inline stuff
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print("this is the output:\n", html)
        self.assertEqual(
            html,
            "<div><ul><li>This is text that <i>should</i> remain</li><li>the <b>same</b> even with inline stuff</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is text that _should_ remain
2. the **same** even with inline stuff
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print("this is the output:\n", html)
        self.assertEqual(
            html,
            "<div><ol><li>This is text that <i>should</i> remain</li><li>the <b>same</b> even with inline stuff</li></ol></div>",
        )


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        header = "# This is some title    "
        self.assertEqual(extract_title(header), "This is some title")

