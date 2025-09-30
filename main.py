
from stats import get_num_words, get_num_of_char, sort_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_num_words(get_book_text(sys.argv[1]))
    num_chars = get_num_of_char(get_book_text(sys.argv[1]))
    sorted_list = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character count ---------")
    for e in sorted_list:
        if e["char"].isalpha():
            print(f"{e["char"]}: {e["num"]}")
    print("============ END ============")
    #print(sys.argv[1])

main()