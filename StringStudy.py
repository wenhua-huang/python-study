if __name__ == '__main__':
    word = '字符串'
    sentence = '这是一个句子'
    # 这个也是注释
    """
    这个是注释
    """
    paragraph = """这是一个段落可以，
    有多行组成"""
    print(word)
    print(sentence)
    print(paragraph)
    print('----------------------')


    str = '123456789'
    print(str) #输出字符串 123456789
    print(str[0:-1]) #输出 从第一个到倒数第二个字符串 12345678
    print(str[0]) # 输出 第一个字符串 1
    print(str[2:5]) # 输出第三个到第五个字符串 345
    print(str[2:]) # 输出第三个到最后一个字符串 3456789
    print(str[1:5:2])  # 从第二个开始 到第五个 每隔两个 24
    print(str * 2) #输出字符串两次
    print(str +"你好") # 链接字符串
    print('----------------------')
    print('hello\nrunoob') # 使用反斜杠转义
    print(r'hello\nruuoob') # 字符串前面添加一个r 表示不会发生转义
    print('\n')
    print(r'\n')



