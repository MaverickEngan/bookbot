from stats import get_num_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = count_characters(book_text)
    sorted_count = sort_characters(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_count)):
        if sorted_count[i]["char"].isalpha():
            print(f"{sorted_count[i]['char']}: {sorted_count[i]['num']}")
main()