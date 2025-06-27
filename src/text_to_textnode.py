from parse_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnode(text: str):
    res = [TextNode(text, TextType.TEXT)]
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    res = split_nodes_delimiter(res, "**", TextType.BOLD)
    res = split_nodes_delimiter(res, "_", TextType.ITALIC)
    return split_nodes_delimiter(res, "`", TextType.CODE)
    
