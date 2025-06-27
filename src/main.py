import os
import shutil
from generate_page import generate_page, generate_pages_recursive
import sys

def recursive_copy(path_from, dist):
    for item in os.listdir(path_from):
        path_item = os.path.join(path_from, item)
        if os.path.isdir(path_item):
            recursive_copy(path_item, dist)
        else:
            path_to = ""
            if len(path_from.split('/')) > 2:
                path_to = path_from.split('/', 2)[2]

            path_to = os.path.join(dist,path_to)
            os.makedirs(path_to, exist_ok=True)
            path_to = os.path.join(path_to, item)

            shutil.copy(path_item, path_to)


def main():
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    public = "docs"
    # public = "./public"
    if os.path.isdir(public):
        shutil.rmtree(public)

    os.mkdir(public)
    recursive_copy("./static", public)

    generate_pages_recursive("content", "template.html", public, basepath)



if __name__ == "__main__":
    main()
