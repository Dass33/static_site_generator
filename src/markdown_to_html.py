from block_type import BlockType, block_to_block_type
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
import re
from parentnode import ParentNode
from text_to_html import text_node_to_html_node
from text_to_textnode import text_to_textnode

def text_to_children(block: str):
    text_nodes = text_to_textnode(block)
    res = []
    for node in text_nodes:
        res.append(text_node_to_html_node(node))
    return res

def get_list_children(body: str):
    res = []
    for node in body.split('\n'):
        res.append(ParentNode(tag='li', children=text_to_children(node)))
    return res


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        stripped_block = re.sub(r' +', ' ', block.replace('\t', ' '))

        match block_type:
                case BlockType.CODE:
                    body = re.sub(r"```", '', block, re.DOTALL)
                    nodes.append(ParentNode(tag='pre', children=[LeafNode(tag="code", value=body)]))

                case BlockType.HEADING:
                    heading_level = len(stripped_block) - len(stripped_block.lstrip('#'))
                    nodes.append(ParentNode(tag=f'h{heading_level}', children=text_to_children(stripped_block.lstrip('#').strip())))
                
                case BlockType.PARAGRAPH:
                    nodes.append(ParentNode(tag='p', children=text_to_children(stripped_block)))

                case BlockType.QUOTE:
                    lines = stripped_block.split('\n')
                    body = '\n'.join(re.sub(r"^>", "", line).strip() for line in lines)
                    nodes.append(ParentNode(tag='blockquote', children=text_to_children(body)))

                case BlockType.UNORDERED_LIST:
                    body = re.sub(r"^- ", '', stripped_block, flags=re.MULTILINE)
                    children = get_list_children(body)
                    nodes.append(ParentNode(tag='ul', children=children))

                case BlockType.ORDERED_LIST:
                    body = re.sub(r"^\d+. ", '', stripped_block, flags=re.MULTILINE)
                    children = get_list_children(body)
                    nodes.append(ParentNode(tag='ol', children=children))

    return ParentNode(tag='div', children=nodes)
