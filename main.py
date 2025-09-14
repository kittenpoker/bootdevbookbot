
import sys
from stats import word_count
from stats import char_count
from stats import chars_list


if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:    
    bookpath = (sys.argv[1])
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {bookpath}...")
    print ("----------- Word Count -----------")
    print (f"Found {word_count(bookpath)} total words")
    print ("--------- Character Count ---------")
    charslist = chars_list(bookpath)
    for char in charslist:
        print (f'{char["char"]}: {char["num"]}')
    print ("============ END =============")
