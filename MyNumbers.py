class MyNumbers:
    def __iter__(self):
        # todo .a 怎么来的 
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

if __name__ == '__main__':

  myclass = MyNumbers()
  myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
