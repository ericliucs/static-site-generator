import unittest
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Go to Google", {"href": "https://google.com"})
        self.assertEqual(node.to_html(),
                         "<a href=\"https://google.com\">Go to Google</a>")
