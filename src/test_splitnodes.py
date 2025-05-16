import unittest
from splitnodes import split_nodes_delimeter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_bold(self):
        node = TextNode("this is a **bold** test", TextType.NORMAL_TEXT)
        node_list = [node]
        self.assertEqual(split_nodes_delimeter(node_list, "**", TextType.BOLD_TEXT), [TextNode("this is a ", TextType.NORMAL_TEXT), TextNode("bold", TextType.BOLD_TEXT), TextNode(" test", TextType.NORMAL_TEXT)])

    def test_italic(self):
        node = TextNode("this is an _italic_ test", TextType.NORMAL_TEXT)
        node_list = [node]
        self.assertEqual(split_nodes_delimeter(node_list, "_", TextType.ITALIC_TEXT), [TextNode("this is an ", TextType.NORMAL_TEXT), TextNode("italic", TextType.ITALIC_TEXT), TextNode(" test", TextType.NORMAL_TEXT)])

    def test_multiples(self):
        node1 = TextNode("this is **a** **multiples** test", TextType.NORMAL_TEXT)
        node2 = TextNode("multiples **multiples** **and** multiples", TextType.NORMAL_TEXT)
        node_list = [node1, node2]
        self.assertEqual(split_nodes_delimeter(node_list, "**", TextType.BOLD_TEXT),
                         [TextNode("this is ", TextType.NORMAL_TEXT), TextNode("a", TextType.BOLD_TEXT), TextNode(" ", TextType.NORMAL_TEXT), 
                          TextNode("multiples", TextType.BOLD_TEXT), TextNode(" test", TextType.NORMAL_TEXT), TextNode("multiples ", TextType.NORMAL_TEXT),
                          TextNode("multiples", TextType.BOLD_TEXT), TextNode(" ", TextType.NORMAL_TEXT), TextNode("and", TextType.BOLD_TEXT),
                          TextNode(" multiples", TextType.NORMAL_TEXT)])



if __name__ == "__main__":
    unittest.main()