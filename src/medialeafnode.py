from leafnode import LeafNode

class MediaLeafNode(LeafNode):
    def __init__(self, tag, props=None):
        super().__init__(tag, "", props)

    def to_html(self):
        return f"<{self.tag} {self.props_to_html()}>"