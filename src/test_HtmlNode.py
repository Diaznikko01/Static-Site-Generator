import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()