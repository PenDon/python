def search_str(s: str) -> str:
    """
    leetcode - 1392
    ababab => abab
    :param s:
    :return:
    """
    char_first = s[0]
    for i in range(1, len(s)):
        if s[i] == char_first:
            if s[:len(s) - i] == s[i:]:
                return s[:len(s) - i]
        else:
            continue
    return ""


s1 = "level"
print(search_str(s1))

