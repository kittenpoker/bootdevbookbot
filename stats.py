def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(bookname):
    book_text = get_book_text("books/"+bookname+".txt")
    words = book_text.split()
    print(f"{len(words)} words found in the document")

def char_count(bookname):
    book_text = get_book_text("books/"+bookname+".txt")
    chars = {}
    for char in book_text.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] = chars[char] +1
    return (chars)
