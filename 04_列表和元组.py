'''列表'''
# extend
list = [1, 3, "4", 1]
list.extend([5,6,7])
list.extend("hello")
print(list)
# append
list.append("hello")
list.append([5,6,7])
print(list)
# insert
list.insert(1,"xiaoming")
print(list)
# del
del list[0]
print(list)
# pop
print(list.pop())
print(list)

""""元组 ： 可以储存多个不可以被修改的数据列表"""
tuple = (1,2,3)
print(type(tuple),"tuple:" ,tuple)

print(tuple)



