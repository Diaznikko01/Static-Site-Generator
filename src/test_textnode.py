import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("textnode", TextType.BOLD_TEXT)
        node2 = TextNode("textnode2", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_not_TextNode(self):
        node = TextNode("stinky", TextType.BOLD_TEXT)
        num = 0
        self.assertNotEqual(node, num)

    def test_eq_w_url(self):
        node = TextNode("sammy", TextType.BOLD_TEXT, "lickthebutt.edu")
        node2 = TextNode("sammy", TextType.BOLD_TEXT, "lickthebutt.edu")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a test", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a test")

    def test_italic(self):
        node = TextNode("This is a test", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a test")

    def test_code(self):
        node = TextNode("This is test code", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is test code")

    def test_link(self):
        node = TextNode("Anchor Text", TextType.LINK, "testurl")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Anchor Text")
        self.assertEqual(html_node.props, {"href": "testurl"})
    
    def test_img(self):
        node = TextNode("Alt Text", TextType.IMAGE, "testurl")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "testurl", "alt": "Alt Text"})


if __name__ == "__main__":
    unittest.main()