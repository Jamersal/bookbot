import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    
    character_counts = count_characters(book_text)
    sorted_characters = sort_characters(character_counts)
    
    print("charcter counts:")
    for char, count in sorted_characters:
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()