def test1():
    num_int = 123
    num_flo = 1.23
    num_new = num_int + num_flo
    print("datatype of num_int:", type(num_int))
    print("datatype of num_flo:", type(num_flo))
    print("Value of num_new:", num_new)
    print("datatype of num_new:", type(num_new))

def test2():
    num_int = 123
    num_str = "456"

    print("Data type of num_int:", type(num_int))
    print("Data type of num_str:", type(num_str))

    # print(num_int + num_str)
def test3():
    num_int = 123
    num_str = "456"

    print("num_int 数据类型为:", type(num_int))
    print("类型转换前，num_str 数据类型为:", type(num_str))

    num_str = int(num_str)  # 强制转换为整型
    print("类型转换后，num_str 数据类型为:", type(num_str))

    num_sum = num_int + num_str

    print("num_int 与 num_str 相加结果为:", num_sum)
    print("sum 数据类型为:", type(num_sum))

if __name__ == '__main__':
    # test1()
    # test2()
    test3()


