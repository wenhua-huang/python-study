import sys

print('命令行参数如下')
for i in sys.argv:
    print(i)
    print("\n\npython路径为：", sys.path, '\n')
