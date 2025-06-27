from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props=None) -> None:
        super(ParentNode, self).__init__(tag=tag, children=children, props=props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Should have a tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("Should have children")

        child_res = ""
        for child in self.children:
            child_res += child.to_html()

        return "<" + self.tag + self.props_to_html() + ">" + child_res + "</" + self.tag + ">"

