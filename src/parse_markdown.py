from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    res = []

    for item in old_nodes:
        item_splited = item.text.split(delimiter)
        for i in range(0, len(item_splited)):
            if len(item_splited[i]) == 0:
                continue
            if i % 2 == 0:
                tmp = TextNode(text=item_splited[i], text_type=item.text_type, url=item.url)
            else:
                tmp = TextNode(text=item_splited[i], text_type=text_type)
            res.append(tmp)

    return res


import re

def split_nodes_image(old_nodes):
    res = []
    for item in old_nodes:
        tmp = item.text
        img_regex = re.findall(r"\!\[.*?\]\(.*?\)", item.text)

        if len(img_regex) == 0:
            res.append(TextNode(text=item.text, text_type=item.text_type, url=item.url))
            continue

        for image in img_regex:
            text, tmp = tmp.split(image, 1)

            if len(text) > 0:
                res.append(TextNode(text=text, text_type=item.text_type, url=item.url))

            res.append(TextNode(text=re.findall(r"\[(.*?)\]", image)[0], text_type=TextType.IMAGE, url=re.findall(r"\((.*?)\)", image)[0]))

        if len(tmp) > 0:
            res.append(TextNode(text=tmp, text_type=item.text_type))

    return res


def split_nodes_link(old_nodes):
    res = []
    for item in old_nodes:
        tmp = item.text
        link_regex = re.findall(r"\[.*?\]\(.*?\)", item.text)

        if len(link_regex) == 0:
            res.append(TextNode(text=item.text, text_type=item.text_type, url=item.url))
            continue

        for link in link_regex:
            text, tmp = tmp.split(link, 1)

            if len(text) > 0:
                res.append(TextNode(text=text, text_type=item.text_type, url=item.url))

            res.append(TextNode(text=re.findall(r"\[(.*?)\]", link)[0], text_type=TextType.LINK, url=re.findall(r"\((.*?)\)", link)[0]))


        if len(tmp) > 0:
            res.append(TextNode(text=tmp, text_type=item.text_type))

    return res
