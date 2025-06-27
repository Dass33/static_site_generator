import unittest
from block_type import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        res_type = block_to_block_type("# This is a heading")
        self.assertEqual(res_type, BlockType.HEADING)

    def test_paragraph(self):
        res_type = block_to_block_type("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.")
        self.assertEqual(res_type, BlockType.PARAGRAPH)
        
    def test_code(self):
        res_type = block_to_block_type("""```
This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
```""")
        self.assertEqual(res_type, BlockType.CODE)

    def test_unordered_list(self):
        res_type = block_to_block_type(
"""- This is the first list item in a list block
- This is a list item
- This is another list item""")
        self.assertEqual(res_type, BlockType.UNORDERED_LIST)


    def test_quote(self):
        res_type = block_to_block_type(
""">This is the first list item in a list block
>This is a list item
>This is another list item""")
        self.assertEqual(res_type, BlockType.QUOTE)

    def test_ordered_list(self):
        res_type = block_to_block_type(
"""1. This is the first list item in a list block
1. This is a list item
2. This is another list item""")
        self.assertEqual(res_type, BlockType.ORDERED_LIST)
