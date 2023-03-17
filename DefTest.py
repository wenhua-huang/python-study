def hello():
    print("hello")
def max(a,b):
    if (a>b):
        return a
    else:
        return b


def changeTest(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
def printinfo1( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
def printinfo( arg, *vartup ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg)
   print (vartup)
def printinfo2( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
def myfunc(n):
  return lambda a : a * n
def sum( arg1, arg2 ):
    total = arg1 + arg2
    print("函数内 : ", total)
    return total

if __name__ == '__main__':
    print("------------hello------------------")
    hello()
    print("------------max------------------")
    a = 4
    b = 5
    print(max(a,b))
    print("---------ref---------------------")
    a = 1
    print(id(a))
    changeTest(a)
    print("---------调用changeme函数---------------------")
    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值: ", mylist)
    print("---------param desc---------------------")
    printinfo1(age=a, name=" runoob")
    print("----------可变参数------------")
    printinfo(70, 60, 50)
    print("----------可变参数 字典------------")
    printinfo2(1, a=2, b=3)
    print("----------lambda------------")
    x = lambda a: a + 10
    print(x(5))

    print("----------lambda arg two------------")
    sum = lambda arg1, arg2: arg1 + arg2
    print(x(5))
    print("相加后的值为 : ", sum(10, 20))
    print("相加后的值为 : ", sum(20, 20))

    print("----------lambda myfunc------------")
    mydoubler = myfunc(2)
    mytripler = myfunc(3)
    print(mydoubler(11))
    print(mytripler(11))
    print("----------return ------------")
    total = sum(10, 20)
    print("函数外 : ", total)
