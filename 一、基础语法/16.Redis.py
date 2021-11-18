def init():
    '''初始化'''
    print("init")

def readValueFromRedis(key):
    print("read")


if __name__ == "__main__":
    init()
    readValueFromRedis("1")