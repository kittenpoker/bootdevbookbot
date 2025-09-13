

def main(bookname):
    book = "books/"+bookname+".txt"
    book_text = get_book_text(book)
    print (book_text)

from stats import word_count
from stats import char_count



word_count("frankenstein")
charcount = char_count("frankenstein")
print (charcount)