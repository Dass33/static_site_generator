from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value: str, props=None) -> None:
        super(LeafNode, self).__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Should contain a value")
        if self.tag == None:
            return self.value
        
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
