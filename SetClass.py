# set 无序去重集合
if __name__ == '__main__':
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
    print(sites)  # {'Google', 'Runoob', 'Zhihu', 'Taobao', 'Facebook', 'Baidu'}
    # 成员测试
    if 'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob 不在集合中')

    a = set('abracadabra')
    b = set('alacazam')
    print(a)  # {'d', 'r', 'a', 'c', 'b'}
    print(a - b)  # a和b 的差集 {'b', 'r', 'd'}
    print(a | b)  # a 和 b的并集 {'r', 'd', 'z', 'm', 'b', 'l', 'a', 'c'}
    print(a & b)  #  a 和 b 的交集 {'a', 'c'}
    print(a ^ b)  # a 和 b 中不同时存在的元素 {'d', 'z', 'r', 'l', 'm', 'b'}

