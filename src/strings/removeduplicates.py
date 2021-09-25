"""
removes duplicate characters from a string in place, without assigning extra memory
for a string buffer.
"""


def remove_duplicates(s):
    # copying here as python strings are immutable
    char_list = list(s)
    char_set = set()

    i = len(char_list) - 1
    pointer = len(char_list) - 1

    while i >= 0:
        char = char_list[i]
        if char not in char_set:
            char_list[pointer] = char
            pointer -= 1
        i -= 1
        char_set.add(char)

    # no extra memory used here as a slice only copies the reference, doesnt make a copy
    return "".join(char_list[pointer + 1:])
