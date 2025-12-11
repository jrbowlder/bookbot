import sys
from stats import word_count, char_count, sort_dict


def get_book_text(filepath):

    with open(filepath) as text:
        file_contents = text.read()

    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1)
    else: 
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_sum = word_count(text)
    counts = char_count(text)
    sort_dict_counts = sort_dict(counts)

              

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_sum} total words.")
    print("--------- Character Count -------")

    for item in sort_dict_counts:
        ch = item["char"]
        num = item["num"]

        if not ch.isalpha():
            continue
        else:
            print(f"{ch}: {num}")

    


main()


