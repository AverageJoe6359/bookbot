def main():
    print(get_book_text("books/frankenstein.txt"))
    
def get_book_text(filepath):
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
        return book_text
main()