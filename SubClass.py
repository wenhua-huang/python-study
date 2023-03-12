# 子类
class A:
    a = 100


class B(A):
    b = 100


if __name__ == '__main__':
    isSame: bool = isinstance(A(), A)
    print(isSame)
    print(type(A()) == A)
    print(isinstance(B(), A))
    print(type(B()) == A)
    print(issubclass(bool, int))
    var1 = 1
    var2 = 10
    print(var2)
    print(var1)
    del var1, var2
