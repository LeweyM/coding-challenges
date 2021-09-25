def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}
    for i in range(len(s1)):
        char_1 = s1[i]
        char_2 = s2[i]
        if char_1 in char_count:
            char_count[char_1] += 1
        else:
            char_count[char_1] = 1

        if char_2 in char_count:
            char_count[char_2] -= 1
        else:
            char_count[char_2] = -1

    for char in char_count:
        if char_count[char] != 0:
            return False

    return True
