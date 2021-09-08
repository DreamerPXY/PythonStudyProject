class Washer():
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def __str__(self):
       return "高："+str(self.height)+"宽："+str(self.width)
    def wash(self):
        print("我可以洗衣服")


w = Washer(12.2,14.5)
w.wash()
print(w)