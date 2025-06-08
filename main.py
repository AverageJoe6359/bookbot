from stats import get_num_characters, get_num_words, sorted_char
import sys
if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]

def main(file_path):
    
    current_text = get_book_text(file_path)
    words = get_num_words(current_text)
    char = get_num_characters(current_text)
    sorted_dict = sorted_char(char)
    

    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing bookfound at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for ch in sorted_dict:
        print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text



main(file_path)