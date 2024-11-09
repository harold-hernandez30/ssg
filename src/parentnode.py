from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent nodes must have a tag")
        
        if not self.children:
            raise ValueError("Empty parent node. Must have children. Consider using LeafNode")
        
        children_node_string = "".join(map(lambda child: child.to_html(), self.children))

        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{children_node_string}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_node_string}</{self.tag}>"