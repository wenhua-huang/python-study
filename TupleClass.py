#  Tuple 不可改变的list
if __name__ == '__main__':
    tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
    print(tuple)  # ('abcd', 786, 2.23, 'runoob', 70.2)

    tinytuple = (123, 'runoob')
print(tuple)  # ('abcd', 786, 2.23, 'runoob', 70.2)

print(tuple[0])  # abcd

print(tuple[1:3])  # (786, 2.23)

print(tuple[2:])  # (2.23, 'runoob', 70.2)
print(tinytuple * 2)  # (123, 'runoob', 123, 'runoob')

print(tuple + tinytuple)  # ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')
