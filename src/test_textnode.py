import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()