if __name__ == '__main__':
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a + b