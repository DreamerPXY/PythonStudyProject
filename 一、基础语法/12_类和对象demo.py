class digua():
    def __init__(self):
        self.time = 0
        self.status = "生的"
        self.condiments = []
    def __str__(self):
        return f"烤了：{self.time},这个地瓜是：{self.status},使用的作料有：{self.condiments}"

    def cook(self,time):
        self.time += time
        if self.time  > 10 :
            self.status = "半生不熟"
        if self.time > 15 :
            self.status = "差不多熟了"
        if self.time > 20:
            self.status = "熟了"
    def add_condiment(self,condiment):
        self.condiments.append(condiment)

dg = digua()
dg.cook(100)
dg.add_condiment("辣椒酱")
dg.add_condiment("甜面酱")
print(dg)
