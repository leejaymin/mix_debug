class Foo:

    def bar(self):
        from ctypes import string_at
        string_at(0xDEADBEEF) # this code will cause Python to segfault


def main():
    f = Foo()
    f.someattr = 42
    f.someotherattr = {'one':1, 'two':2, 'three':[(), (None,), (None, None)]}
    f.bar()


if __name__ == "__main__":
    main()
