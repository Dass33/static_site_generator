from block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        stripped_block = block.strip()
        heading_level = len(stripped_block) - len(stripped_block.lstrip('#'))

        stripped_block = stripped_block.lstrip('#')
        stripped_block = stripped_block.strip()

        if block_type == BlockType.HEADING and heading_level == 1:
            return stripped_block

    raise Exception("Header is missing")
