def dec1(func):
    print("1111")

    def one():
        print("2222")
        func()
        print("3333")
        return 1+3

    return one


def dec2(func):
    print("aaaa")

    def two():
        print("bbbb")
        func()
        print("cccc")
        return 1+2

    return two


"""
这里的装饰器等同于赋值语句： test = dec1(dec2(test)) 执行test()时  等同于 执行 dec1(dec2(test))()
dec2(test) 的结果是 返回一个 two 函数, dec1(two) 的结果返回一个 one 函数, 因此最后执行 one() 在执行 two
"""


@dec1
@dec2
def test():
    print("test test")
    return 1+1


print(test())
