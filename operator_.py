#
"""
算术运算
"""
def arithmetic():
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c 的值为：", c)

    c = a - b
    print("2 - c 的值为：", c)

    c = a * b
    print("3 - c 的值为：", c)

    c = a / b
    print("4 - c 的值为：", c)

    c = a % b
    print("5 - c 的值为：", c)

    # 修改变量 a 、b 、c
    a = 2
    b = 3
    c = a ** b
    print("6 - c 的值为：", c)

    a = 10
    b = 5
    c = a // b
    print("7 - c 的值为：", c)


def compare():
    a = 21
    b = 10
    c = 0

    if a == b:
        print("1 - a 等于 b")
    else:
        print("1 - a 不等于 b")

    if (a != b):
        print("2 - a 不等于 b")
    else:
        print("2 - a 等于 b")

    if (a < b):
        print("3 - a 小于 b")
    else:
        print("3 - a 大于等于 b")

    if (a > b):
        print("4 - a 大于 b")
    else:
        print("4 - a 小于等于 b")

    # 修改变量 a 和 b 的值
    a = 5
    b = 20
    if (a <= b):
        print("5 - a 小于等于 b")
    else:
        print("5 - a 大于  b")

    if (b >= a):
        print("6 - b 大于等于 a")
    else:
        print("6 - b 小于 a")


def assignment():
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c 的值为：", c)

    c += a
    print("2 - c 的值为：", c)

    c *= a
    print("3 - c 的值为：", c)

    c /= a
    print("4 - c 的值为：", c)

    c = 2
    c %= a
    print("5 - c 的值为：", c)

    c **= a
    print("6 - c 的值为：", c)

    c //= a
    print("7 - c 的值为：", c)


def bit():
    a = 0o0111100

    b = 0o0001101


    print(a & b) # 0o0001100

    print(a | b )# 0011 1101

    print(a ^ b)  # 00110001

    print(~a)  # 11000011


def bit2():
    a = 60  # 60 = 0011 1100 
    b = 13  # 13 = 0000 1101 
    c = 0

    c = a & b  # 12 = 0000 1100
    print("1 - c 的值为：", c)

    c = a | b  # 61 = 0011 1101 
    print("2 - c 的值为：", c)

    c = a ^ b  # 49 = 0011 0001
    print("3 - c 的值为：", c)

    c = ~a  # -61 = 1100 0011
    print("4 - c 的值为：", c)

    c = a << 2  # 240 = 1111 0000
    print("5 - c 的值为：", c)

    c = a >> 2  # 15 = 0000 1111
    print("6 - c 的值为：", c)


def logic():
    a = 10
    b = 20

    if (a and b):
        print("1 - 变量 a 和 b 都为 true")
    else:
        print("1 - 变量 a 和 b 有一个不为 true")

    if (a or b):
        print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("2 - 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if (a and b):
        print("3 - 变量 a 和 b 都为 true")
    else:
        print("3 - 变量 a 和 b 有一个不为 true")

    if (a or b):
        print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("4 - 变量 a 和 b 都不为 true")

    if not (a and b):
        print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5 - 变量 a 和 b 都为 true")


def list_element():
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if (a in list):
        print("1 - 变量 a 在给定的列表中 list 中")
    else:
        print("1 - 变量 a 不在给定的列表中 list 中")

    if (b not in list):
        print("2 - 变量 b 不在给定的列表中 list 中")
    else:
        print("2 - 变量 b 在给定的列表中 list 中")

    # 修改变量 a 的值
    a = 2
    if (a in list):
        print("3 - 变量 a 在给定的列表中 list 中")
    else:
        print("3 - 变量 a 不在给定的列表中 list 中")


def is_not_is():
    a = 20
    b = 20

    if (a is b):
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if (id(a) == id(b)):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if (a is b):
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if (a is not b):
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")


def priority():
    pass


if __name__ == '__main__':
    arithmetic()
    print("--------------------------------------")
    compare()
    print("------------------------------------")
    assignment()
    print("--------------------------------------")
    bit()
    print("--------------------------------------")
    bit2()
    print("--------------------------------------")
    logic()
    print("-------------------")
    list_element()
    print("---------------")
    is_not_is()
    print("---------------")
    priority()



