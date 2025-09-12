def get_book_text(book):
    with open(book) as f:
        return f.read()

def main(bookname):
    book = "books/"+bookname+".txt"
    book_text = get_book_text(book)
    print (book_text)

main("frankenstein")