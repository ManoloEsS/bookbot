import stats


def get_book_text(file: str):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def print_stats(file: str, words: int, dict_list: list):
    print(f"{' BOOKBOT ':=^33}")
    print(f"Analyzing book found at {file}...")
    print(f"{' Word Count ':-^33}")
    print(f"Found {words} total words")
    print(f"{' Character Count ':-^33}")
    for dict in dict_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print(f"{' END ':=^33}")


def main(book: str):
    contents = get_book_text(book)
    word_count = stats.count_words(contents)
    character_count = stats.count_char(contents)
    sorted = stats.sorted_list(character_count)
    # print(f"{word_count} words found in the document")
    # print(character_count)
    # print(sorted_list(character_count))
    print_stats(book, word_count, sorted)


if __name__ == "__main__":
    main("books/frankenstein.txt")
