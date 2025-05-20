def get_book_text(file: str):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def count_words(contents: str):
    words = []
    words = contents.split()
    return len(words)


def main(book: str):
    contents = get_book_text(book)
    count = count_words(contents)
    print(f"{count} words found in the document")


if __name__ == "__main__":
    main("books/frankenstein.txt")
