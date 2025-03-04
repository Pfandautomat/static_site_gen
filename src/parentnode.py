from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Children cannot be None or an empty list for ParentNode")

    
    def to_html(self):
        
        full_html = []
        full_html.append(f"<{self.tag}{self.props_to_html()}>")

        for child in self.children:

            full_html.append(child.to_html())
        
        full_html.append(f"</{self.tag}>")
        return "".join(full_html)


            


