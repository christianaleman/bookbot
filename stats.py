def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_book_number_words(text: str) -> int:
    words = text.split()
    return len(words)