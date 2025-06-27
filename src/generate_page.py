from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    f = open(from_path, mode='r')
    markdown = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    f = open(template_path, mode='r')
    template = f.read()

    filled_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(filled_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        path_item = os.path.join(dir_path_content, item)
        if os.path.isdir(path_item):
            generate_pages_recursive(path_item, template_path, dest_dir_path)
        else:
            path_to = ""
            if len(dir_path_content.split('/')) > 1:
                path_to = dir_path_content.split('/', 1)[1]

            path_to = os.path.join(dest_dir_path,path_to)
            os.makedirs(path_to, exist_ok=True)
            new_item = item.rstrip(".md") + ".html"
            path_to = os.path.join(path_to, new_item)

            generate_page(path_item, template_path, path_to)
