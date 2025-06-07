def main():
    print(get_book_text("books/frankenstein.txt"))
    
def get_book_text(filepath):
    with open("frankenstein.txt", encoding="utf-8") as f:
        book_text = f.read()
main()