from textnode import TextType, TextNode


def main() -> None:
    test_textnode: TextNode = TextNode("Anchor text", TextType.LINK,
                                       "https://www.boot.dev")
    print(test_textnode)


if __name__ == '__main__':
    main()
