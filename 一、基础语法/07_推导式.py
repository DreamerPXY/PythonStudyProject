'''old'''
i = 0
list = []
while i < 10:
    list.append(i)
    i+=1
print(list)

list.clear()
print(list)
'''推导式'''

list = [i for i in range(10)]
print(list)

'''带if的推导式'''
list.clear()
list = [i for i in range(10) if i%2 == 0]
print(list)

'''双重for循环的推导式'''
list.clear()
list = [(i,j) for i in range(6) for j in range(5)]
print(list)

"""字典推导式"""
map = {i : i**2 for i in range(3)}
print(map)

keys = ["name","age","sex"]
values = ["张三",12,1]
map.clear()
map = {keys[i]:values[i] for i in range(len(keys))}
print(map)