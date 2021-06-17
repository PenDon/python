def circle(n: list, m: int):
    """

    :param n:
    :param m:
    :return:
    """
    length = len(n)
    if length == 1:
        return n
    else:
        if length >= m:
            newList = reverse(n, m)
            print(f"The No.{n[m - 1]} quit the game")
        else:
            index = m % length
            newList = reverse(n, index)
            print(f"The No.{n[index - 1]} quit the game")

        print(f"Survived List:{newList}")
        return circle(newList, m)


def reverse(n: list, index: int):
    if index:
        reverseList = n[index:]
        reverseList.extend(n[:index - 1])
    else:
        reverseList = n[:-1]
    return reverseList


n1 = eval(input("Enter the number of n:"))

m1 = eval(input("Enter the number of m:"))

survived_list = list(range(1, n1 + 1))

circle(survived_list, m1)
# print(survived_list)
