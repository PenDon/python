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


# charCount()


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


# stringReverse()

def shopping():
    """
    shopping plan
    :return:
    """
    total, num = input().split(" ")
    lis = []
    num = eval(num)
    total = eval(total)
    for i in range(num):
        v, p, q = input().split(" ")
        lis.append([eval(v), eval(p) * 100, eval(q)])

    print(lis)
    # todo 学习动态规划相关算法 - 背包算法相关


# shopping()
# shopping 测试数据集
"""
2000 10
500 1 0
400 4 0
300 5 1
400 5 1
200 5 0
500 4 5
400 4 0
320 2 0
410 3 0
400 3 5
"""



"""
2000 10
500 1 0 1
400 4 0 2
300 5 1 3
400 5 1 4
200 5 0 5
500 4 5 6
400 4 0 7
320 2 0 8
410 3 0 9
400 3 5 10
"""
def delete_string():
    """
    删除出现次数最少的字符
    :return:
    """
    string = input()
    dic = {}
    for s in string:
        if s in dic.keys():
            dic[s] += 1
        else:
            dic[s] = 1
    max_num = max(dic.values())
    print(max_num)

delete_string()