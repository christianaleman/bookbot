from stats import get_book_text, get_book_number_words, get_book_number_chars, sorted_characters
import sys

def main():
    if len(sys.argv) < 2:   
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(f'{sys.argv[1]}')  
    print(f"============ BOOKBOT ============")
    print(f'Analyzing book found at ... {sys.argv[1]}')
    print("----------- Character Count ----")
    print("----------- Word Count ----------")
    num_words = get_book_number_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    a = sorted_characters(get_book_number_chars(text))
    for char in a:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
           


    


if __name__ == "__main__":
    main()
