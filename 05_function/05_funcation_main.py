from funcation_model1 import foo
from funcation_model2 import foo

foo()
def shuoming():
    '''测试说明文档'''
    pass
def main(*args):
    data = 0
    for i in args:
        data += i
    return data

if __name__ =="__main__":
    print(main(1,2,3,4))
    help(shuoming)