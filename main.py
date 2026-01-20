from stats import find_words, count_chars
import sys
import os
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
if os.path.exists(path):
    pass
else:
    print("File Path not Found")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    print(file_contents)


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    find_words(path)
    print("--------- Character Count -------")
    count_chars(path)
    print("============= END ===============")
main()

