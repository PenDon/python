import time

"""
斐波那契数列 拼接为字符串
"""


def fibonacci(n):
    if n == 1:
        return "0"
    if n == 2:
        return "1"
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
fibonacci(35)
# s = fibonacci(35)
# print(s)
end = time.time()
print(f'用时{end - start}s')
"""
n = 35, 平均用时2.7s; Java中平均用时270ms
"""
