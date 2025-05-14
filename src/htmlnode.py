class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        list_to_join = [f' {key}="{value}"' for key, value in self.props.items()]
        return "".join(list_to_join)
    
    def __repr__(self):
        return f"HtmlNode: {self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        html_props = self.props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Requires Tag")
        if self.children == None or not self.children:
            raise ValueError("Requires Children")
        html = "<" + self.tag + ">"
        for child in self.children:
            child_html = child.to_html()
            html += child_html
        return html + "<" + "/" + self.tag  + ">"

