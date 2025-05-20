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


def sort_on(dict):
    return dict["num"]


def sorted_list(chars: dict):
    char_list = []
    for k, v in chars.items():
        char_dict = {}
        char_dict["char"] = k
        char_dict["num"] = v
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
