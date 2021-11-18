class Person(object):
    def __init__(self):
        self.nose = "鼻子"
        self.mource = "嘴巴"
        self.eyes = "眼睛"
    def cook(self):
        print("不是任何人都会做饭")
    def showHands(self):
        print("say hello")

class Student(Person):
    def __init__(self,no):
        self.no = no
    def cook(self):
        print("我还在学做饭")

class Cooker(Person):
    def cook(self):
        print("我会做饭")
    def __init__(self,money,name):
        Person.__init__(self)
        super().__init__()
        self._money = money
        self.name = name
    def getMoney(self):
        return self._money
    def setMoney(self,money):
        self._money = money
    def _showMoney(self):
        print(f"showMoney:{self._money}")


c = Cooker(12777.3,"张三")
c.showHands()
print(c.name)
c.cook()
print(c.getMoney())
c.setMoney(12999.3)
print(c.getMoney())
c._showMoney()
s = Student("123123")
s.cook()
s.showHands()
