import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_difference(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_difference(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is A text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_invalid_url(self):
        self.assertRaises(ValueError, lambda: TextNode("This is an invalid URL",
                                                       TextType.NORMAL,
                                                       "https//bruh.com"))


if __name__ == "__main__":
    unittest.main()
