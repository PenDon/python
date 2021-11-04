import time


def fibonacci(n):
    if n == 1:
        return "0"
    if n == 2:
        return "1"
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
s = fibonacci(5)
print(s)
c = s.count("10")
print(c)
end = time.time()
print(f'用时{end - start}s')
