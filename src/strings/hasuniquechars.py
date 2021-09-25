def has_unique_chars_sorted(s):
    # n space required for sorted string
    s = sorted(s)
    for i in range(len(s)):
        if i + 1 == len(s):
            return True
        if s[i] == s[i + 1]:
            return False
    return True


def has_unique_chars(s):
    # set space is limited to number of chars = 256 for ASCII
    chars = set()
    for c in s:
        if c in chars:
            return False
        chars.add(c)
    return True
