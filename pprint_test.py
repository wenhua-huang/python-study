import pprint, pickle


def test_pprint():
    # 使用pickle模块从文件中重构python对象
    pkl_file = open('D:\Desktop\windows\data.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)
    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)
    pkl_file.close()


if __name__ == '__main__':
    test_pprint()