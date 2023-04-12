from sys import argv, path
from ClassTest import moduleField, moduleDef
import builtins

if __name__ == '__main__':
    print(path)
    print(moduleField)
    moduleDef()
    print(builtins.dir())
