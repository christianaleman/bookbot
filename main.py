from stats import get_book_text, get_book_number_words

def main():
    text = get_book_text("./books/frankenstein.txt")
    number_words = get_book_number_words(text)
    print(f"{number_words} words found in the document")

if __name__ == "__main__":
    main()
