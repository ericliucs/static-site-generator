from typing import Self
from typing_extensions import Optional
from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self,
                 tag: Optional[str] = None,
                 value: Optional[str] = None,
                 children: Optional[list[Self]] = None,
                 props: Optional[dict[str, str]] = None):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[Self] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        html: str = ""
        if self.props is not None:
            for prop, attribute in self.props.items():
                html += f" {prop}=\"{attribute}\""
        return html

    def __repr__(self) -> str:
        return (f"HTMLNode(tag=\"{self.tag}\", "
                f"value=\"{self.value}\", "
                f"children=\"{self.children}\", "
                f"props=\"{self.props_to_html()}\")")


class ParentNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 children: list[HTMLNode],
                 props: Optional[dict[str, str]] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        return self.create_html_tags(self)

    def create_html_tags(self, node: HTMLNode) -> str:
        if not node.children:
            return node.to_html()
        html_tags = f"<{node.tag}{node.props_to_html()}>"
        for child in node.children:
            html_tags += self.create_html_tags(child)
        return f"{html_tags}</{node.tag}>"


class LeafNode(HTMLNode):
    def __init__(self,
                 tag: Optional[str],
                 value: str,
                 props: Optional[dict[str, str]] = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNodes must have a value")
        if self.tag is None:
            return self.value
        else:
            return self.create_html_tag()

    def create_html_tag(self) -> str:
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


def text_node_to_html_node(node: TextNode) -> LeafNode:
    match node.text_type:
        case TextType.TEXT:
            return LeafNode(None, node.text, None)
        case TextType.BOLD:
            return LeafNode("b", node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", node.text, None)
        case TextType.CODE:
            return LeafNode("code", node.text, None)
        case TextType.LINK:
            return LeafNode("a", node.text, {"href": node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": node.url, "alt": node.text})
        case _:
            raise ValueError("Unknown node type")
