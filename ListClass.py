import operator
def reverseWords(input):
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


def testDel():
    list = ['Google', 'Runoob', 1997, 2000]

    print("原始列表 : ", list)
    del list[2]
    print("删除第三个元素 : ", list)


def testAppend():
    squares = [1, 4, 9, 16, 25]
    squares += [36, 49, 64, 81, 100]
    print(squares)


def testNest():
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)


def testEq():
    a = [1, 2]
    b = [2, 3]
    c = [2, 3]
    print("operator.eq(a,b): ", operator.eq(a, b))
    print("operator.eq(c,b): ", operator.eq(c, b))

"""
推倒式
"""
def testCD():
    vec = [2, 4, 6]
    var = [3 * x for x in vec]
    print(var)


if __name__ == '__main__':
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']
    print(list)  # ['abcd', 786, 2.23, 'runoob', 70.2]
    print(tinylist)  # [123, 'runoob']
    print(list[0])  # abcd
    print(list[1:3])  # [786, 2.23]
    print(list[2:])  # [2.23, 'runoob', 70.2]
    print(tinylist * 2)  # [123, 'runoob', 123, 'runoob']
    print(list + tinylist)  # ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

    print('---------------------------------------')
    a = [1, 2, 3, 4, 5, 6]
    a[0] = 9
    print(a)  # [9, 2, 3, 4, 5, 6]

    a[2:5] = [13, 14, 15]
    print(a)  # [9, 2, 13, 14, 15, 6]
    a[2:5] = []
    print(a)  # [9, 2, 6]

    print('------------------------------------')
    intput = 'I like runoob'
    rw = reverseWords(intput)
    print(rw)
    print('----------del--------------------------')
    testDel()
    print('--------------apend-------------')
    testAppend()
    print('-------------nest------------')
    testNest()
    print('------------eq--------')
    testEq()
    print("----------推倒式------")
    testCD()

