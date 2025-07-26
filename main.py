##from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)

    print (f"Found {word_count} total words")
    print("charcter counts:")
    character_counts = count_characters(book_text)

    sorted_characters = sort_characters(character_counts)
   
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    
if __name__ == "__main__":
    main()


