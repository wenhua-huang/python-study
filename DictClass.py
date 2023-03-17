if __name__ == '__main__':
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2] = "2 - 菜鸟工具"
    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print (dict['one'])       # 1 - 菜鸟教程
print (dict[2])           # 2 - 菜鸟工具
print (tinydict)          # {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print (tinydict.keys())   # dict_keys(['name', 'code', 'site'])
print (tinydict.values()) # dict_values(['runoob', 1, 'www.runoob.com'])
 # a  = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
#  字典里没有的键访问数据 会输出错误

