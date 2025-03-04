from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")

    
    def to_html(self):
        raise