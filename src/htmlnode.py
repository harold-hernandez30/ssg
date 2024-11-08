
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Must implement")
    
    def props_to_html(self):
        return " ".join(map(lambda key_val: f'{key_val[0]}="{key_val[1]}"', self.props.items()))
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},children:{self.children},{self.props_to_html()})"