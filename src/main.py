from textnode import TextNode, TextType

def main():
    text = TextNode("This is some anchor text", TextType.L, "https://www.boot.dev")
    print(text)

if __name__ == "__main__":
    main()
