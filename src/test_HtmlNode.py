import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is a test", ['obj1', 'obj2', 'obj3'], {"hello": "world", "poopy": "doopy"})
        self.assertEqual(node.props_to_html(), ' hello="world" poopy="doopy"')
    def test_agian(self):
        node = HTMLNode("h1", "this is a test")
        self.assertEqual(node.props_to_html(), "")
    def test_final(self):
        node = HTMLNode("h1", "this is a test", props={"lard": "face"})
        self.assertEqual(node.props_to_html(), ' lard="face"')
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_url_to_html(self):
        leaf = LeafNode("a", "Click Me!", {"href": "abc.com"})
        self.assertEqual(leaf.to_html(), '<a href="abc.com">Click Me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()