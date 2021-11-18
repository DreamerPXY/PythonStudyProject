def foo():
    print("goodbye world")


def boo():
    print("boo")
    return 1,2,3


if __name__ == '__main__':
    foo()
else:
    x,y,z = boo()
    print("x,y,z:",x,y,z)
