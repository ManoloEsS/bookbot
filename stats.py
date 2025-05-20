def count_words(contents: str):
    words = []
    words = contents.split()
    return len(words)


def count_char(contents: str):
    chars = {}
    lowercase_contents = contents.lower()
    for char in lowercase_contents:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars
