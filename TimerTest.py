from timeit import Timer
def printt():
    print('hello world')
if __name__ == '__main__':
    print(Timer(printt).timeit())