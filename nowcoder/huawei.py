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
        lis.append([eval(v), eval(p), eval(q)])

    print(lis)
    cost_performance = [0] * num
    cost_performance_extra = [0] * num
    for index, element in enumerate(lis):
        # 主件与附件
        if element[2] == 0:
            cost_performance[index] = element[1] * element[0]
        else:
            # 记录一个附件带主件的性价比 以及 选定主件后额外增加一个附件的性价比
            cost_performance[index] = element[1] * element[0] + lis[element[2] - 1][1] * lis[element[2] - 1][0]
            cost_performance_extra[index] = element[1] * element[0]

    print(cost_performance)
    print(cost_performance_extra)
    # 记录购买了哪些物品
    shopping_list = []
    # 记录循环检索了哪些物品, 当所有物品都被检索后, 终止循环
    index_to_check = list(range(num))

    # while total > 0:
    while len(index_to_check):
        # 检索性价比最高的物品编号 - 索引
        max_cost = 0
        print(cost_performance)
        for index_check in index_to_check:
            if cost_performance[index_check] > max_cost:
                max_cost = cost_performance[index_check]
                m = index_check
        # 计算当前物品价格
        s = lis[m][0]
        # 如果当前物品是附件, 并且主件未在购物车内, 额外添加主件价格
        if lis[m][2] != 0 and shopping_list.count(lis[m][2] - 1) == 0:
            s += lis[lis[m][2] - 1][0]
        print(f"当前选中物品{m + 1}, 总价：{s}")
        if total - s >= 0:
            # 买得起, 扣除物品总价
            total = total - s
            print(f"选中{m + 1}号物品！")
            # 索引 m 加入购物车, 更新待检索数组
            shopping_list.append(m)
            print(index_to_check)
            print(m)
            index_to_check.remove(m)
            # 如果当前物品有主件, 并且主件还没在购物车内, 主件加入购物车, 更新该主件的附件性价比
            if lis[m][2] != 0 and shopping_list.count(lis[m][2] - 1) == 0:
                shopping_list.append(lis[m][2] - 1)
                print(index_to_check)
                print(lis[m][2] - 1)
                index_to_check.remove(lis[m][2] - 1)
                # 更新该组件的附件性价比
                index_to_update = []
                for i, ele in enumerate(lis):
                    # 遍历, 检索主件是当前附件的主件的附件, 并且还未加入购物车的附件
                    if ele[2] == lis[m][2] - 1 and i in index_to_check:
                        index_to_update.append(i)
                # 更新待更新的附件性价比
                for j in index_to_update:
                    cost_performance[j] = cost_performance_extra[j]
            else:
                if lis[m][2] == 0:
                    index_to_update = []
                    for i, ele in enumerate(lis):
                        # 遍历, 检索主件是当前附件的主件的附件, 并且还未加入购物车的附件
                        if ele[2] == m + 1 and i in index_to_check:
                            index_to_update.append(i)
                    # 更新待更新的附件性价比
                    for j in index_to_update:
                        cost_performance[j] = cost_performance_extra[j]
        else:
            # 买不起, 移除该性价比, 重新挑选
            print(index_to_check)
            print(m)
            index_to_check.remove(m)
    print(shopping_list)
    summary = 0
    for index_final in shopping_list:
        summary += lis[index_final][0] * lis[index_final][1]
    print(summary)


shopping()
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