import unittest
from text_to_textnode import text_to_textnode
from textnode import TextNode, TextType
from parse_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestTextToHTML(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")

    def test_multiple_bold(self):
        node = TextNode("This is **text** with a **code block** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "text")
        self.assertEqual(new_nodes[3].text, "code block")

    def test_multiple_input(self):
        node = TextNode("This is text with a code block _word_", TextType.TEXT)
        node1 = TextNode("_This_ is text with a code block word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node, node1], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "word")

        self.assertEqual(new_nodes[2].text, "This")
        self.assertEqual(new_nodes[2].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)

class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
        )

    def test_split_no_images(self):
        node = TextNode( "This is text with an and another", TextType.ITALIC,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [TextNode("This is text with an and another", TextType.ITALIC)],
        )

class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node, node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.BOLD),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.BOLD),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with an ", TextType.BOLD),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.BOLD),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
        )

    def test_split_no_links(self):
        node = TextNode( "This is text with an and another", TextType.ITALIC,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [TextNode("This is text with an and another", TextType.ITALIC)],
        )

class TestSplitAll(unittest.TestCase):
    def test_split_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnode(text)
        self.assertEqual(
                new_nodes,
             [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, url="https://boot.dev"),
            ]
        )
