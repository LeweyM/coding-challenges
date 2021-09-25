def reverse(s):
    char_list = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return "".join(char_list)
