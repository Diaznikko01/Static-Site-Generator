from textnode import TextNode, TextType



def split_nodes_delimeter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            node_list.append(node)
        else:
            working_list = node.text.split(delimiter)
            if len(working_list) % 2 == 0:
                raise Exception("Unmatched delimiter")
            else:
                for i in range(0, len(working_list)):
                    if i == 0 or i % 2 == 0:
                        text =  TextNode(working_list[i], TextType.NORMAL_TEXT)
                        node_list.append(text)
                    else:
                        text = TextNode(working_list[i], text_type)
                        node_list.append(text)
    return node_list