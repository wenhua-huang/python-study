# 推导式
def test1():
    names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)


def test2():
    multiples = [i for i in range(30) if i % 3 == 0]
    print(multiples)


def test3():
    listdemo = ['Google', 'Runoob', 'Taobao']
    newdict = {key: len(key) for key in listdemo}
    print(newdict)
    dic = {x: x ** 2 for x in (2, 4, 6)}
    print(dic)


def test4():
    setnew = {i ** 2 for i in (1, 2, 3)}
    print(setnew)
    a = {x for x in 'abreeeacadabra' if x not in 'abc'}# a 是set
    print(type(a))
    print(a)


def test5():
    a = (x for x in range(1, 10))
    print(a)
    print(tuple(a))
    print(a)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()