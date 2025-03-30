from enum import Enum
from typing import Optional


class TextType(Enum):
    TEXT = 0
    BOLD = 1
    ITALIC = 2
    CODE = 3
    LINK = 4
    IMAGE = 5


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        if (url is not None and (text_type is not TextType.LINK and text_type is
                                 not TextType.IMAGE)):
            raise ValueError("Argument url may only be set if argument "
                             "text_type is TextType.LINK or TextType.IMAGE")
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: Optional[str] = url

    def __eq__(self, other: any) -> bool:
        return (self.text == other.text and self.text_type == other.text_type
                and self.url == other.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
