def main():
    from stats import get_num_characters, get_num_words, sorted_char
    

    current_words = get_book_text()
    words = get_num_words(current_words)
    char = get_num_characters(current_words)
    sorted_dict = sorted_char(char)
    
    print("============ BOOKBOT ============")
    print("Analyzing bookfound at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for ch in sorted_dict:
        print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")
def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
        return book_text



main()