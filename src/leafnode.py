from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, None, props)
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode")


    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None for LeafNode")

        if self.tag is None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        



        

        

        
        