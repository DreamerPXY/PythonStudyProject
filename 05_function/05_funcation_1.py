'''返回多个参数 支持参数的拆组'''
def getName():
    return 1,2

result = getName()
print(result)
"""传参测试"""
def userinfo(name,age,sex = 1):
    return name,age,sex

userinfo = userinfo("张三",1)
print(userinfo)

def username(*args):
    print(len(args))
    return args

print(username(1,2,3,4))
print(username("name"))
"""包裹关键字传递"""

def  userfunc(**args):
    return args
print(userfunc(name="张三",age = 12))