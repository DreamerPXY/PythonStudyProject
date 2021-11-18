try:
     i = 1%0
except Exception as result:
    print(result)
finally:
    print("计算失败")

class MyException(Exception):
    def __init__(self,code,msg):
        self.code = code
        self.msg = msg
    def __str__(self):
        return f"发生异常，errCode:{self.code},errMsg:{self.msg}"

try:
    print("模拟发生异常")
    raise MyException(200,"败了败了")
except Exception as result :
    print(result)