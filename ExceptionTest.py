def test_syntax_error():
    return
    # while True print('Hello world')
def test_math_exception() :
    var = 10 * (1 / 0)
    print(var)
    return

def test_try():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")


if __name__ == '__main__':
    while True:
        try:
            x = int(input("请输入一个数字: "))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
