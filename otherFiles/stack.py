def judge(s: str) -> bool:
    """
    (){}() is illegal
    :param s:
    :return:
    """
    while "()" in s:
        s = s.replace("()", "")
    return s == ""
