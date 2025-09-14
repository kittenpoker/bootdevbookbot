def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

def word_count(bookpath):
    book_text = get_book_text(bookpath)
    words = book_text.split()
    #print(f"{len(words)} words found in the document")
    return (len(words))

def char_count(bookpath):
    book_text = get_book_text(bookpath)
    chars = {}
    for char in book_text.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] = chars[char] +1
    return (chars)

def sort_on(items):
    return items["num"]

def chars_list (bookpath):
    charcount = char_count(bookpath)
    charslist = []
    for char, num in charcount.items():
        if char.isalpha():
            charslist.append ({"char": char, "num": num})
    charslist.sort(reverse=True, key=sort_on)
    return (charslist)