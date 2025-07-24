def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_book_number_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_book_number_chars(text: str) -> dict:
    chars_in_text = {}
    for char in text.lower():
        if char not in chars_in_text:
            chars_in_text[char] = 1            
        else:
            chars_in_text[char] += 1
    return chars_in_text

def sort_on(item: dict) -> int:
    return item["num"]

def sorted_characters(char_dict: dict) -> list:
    new_list = []
    for char in char_dict:
        if char.isalpha():
            new_list.append({"char": char, "num": char_dict[char]})
            new_list.sort(reverse=True, key = sort_on)
    return new_list