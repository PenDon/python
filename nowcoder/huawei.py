def charCount():
    """
    Statistics on the number of non duplicate strings
    :return:
    """
    string = input()
    li = []
    for a in string:
        if a in li:
            continue
        else:
            li.append(a)
    print(len(li))


def intReverse():
    """

    :return:
    """
    li = list(input())
    string = ''
    for i in range(len(li)):
        string += li.pop()
    print(string)


# intReverse()

def stringReverse():
    """

    :return:
    """
    li = list(input())
    string = ''
    for i in range(len(li)):
        string += li.pop()
    print(string)


stringReverse()

