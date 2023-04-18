#!/usr/bin/python3
def test_w():
    f = open("D:\Desktop\windows\新建文本文档.txt", "w")
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    # 关闭打开的文件
    f.close()
def test_r():
    f = open("D:\Desktop\windows\新建文本文档.txt","r")
    str = f.readline()
    print(str)
def test_r2():
    f = open("D:\Desktop\windows\新建文本文档.txt","r")
    strs = f.readlines()
    print(strs)
# 打开一个文件
if __name__ == '__main__':
    test_w()