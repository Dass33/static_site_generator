from __future__ import annotations

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Implement it you..")

    def props_to_html(self):
        if self.props == None:
            return ""
        res = ""
        for k,v in self.props.items():
            res += ' ' + k + '=' + '\"' + v + '\"'
        return res

    def __repr__(self) -> str:
        return str(self.tag) + ', ' + str(self.value) + ', ' + str(self.children) + ', ' + self.props_to_html()


