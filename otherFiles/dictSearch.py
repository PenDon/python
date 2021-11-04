import time
b = {
    1: {
        11: {
            111: 150,
            112: 151,
            113: 152,
        },
        12: {
            121: 160,
            122: 161,
            123: 162,
        },
    },
    2: {
        21: {
            211: 0,
            212: 1,
            213: 1,
        },
        22: {
            211: 0,
            212: 1,
            213: 1,
        },
    },
}


def custom_sum(obj):
    """

    :param obj: dict  or int
    :return: summary
    """
    if isinstance(obj, dict):
        summary = 0
        for v in obj.values():
            summary += custom_sum(v)
        return summary
    else:
        return obj


def search(dic: dict, key: int):
    """
    search multiple dict with key
    :param dic:
    :param key:
    :return:
    """
    if not isinstance(dic, dict):
        return None
    print("Current dict:")
    print(dic)
    value = dic.get(key)
    if value:
        return custom_sum(value)
    else:
        for v in dic.values():
            result = search(v, key)
            if result:
                return result
        return None


start = time.time()
print(search(b, 1111))
# print(search(b, 111))
# print(search(b, 11))
# print(search(b, 1))
end = time.time()
print(f"time: {end - start}")
