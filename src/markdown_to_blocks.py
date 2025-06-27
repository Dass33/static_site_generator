def markdown_to_blocks(text: str):
    blocks = text.split("\n\n")
    res = []
    for block in blocks:
        striped_block = block.strip()
        if len(striped_block) == 0:
            continue

        res.append(striped_block)

    return res
