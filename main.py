from stats import count_char, count_words


def get_book_text(file: str):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main(book: str):
    contents = get_book_text(book)
    word_count = count_words(contents)
    character_count = count_char(contents)

    print(f"{word_count} words found in the document")
    print(character_count)


if __name__ == "__main__":
    main("books/frankenstein.txt")
