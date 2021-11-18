def return_num():
    return 100,200

n1,n2 = return_num()
print(n1,n2)


"""拆包字典"""
dict1 = {"name":"彭小余","age":18,"sex":"男"}
a,b,c= dict1
print(a)
print(b)
print(c)

print(dict1[a])
print(dict1[b])
print(dict1[c])


"""交换变量"""

a,b = 1,2
a,b = b,a
print(a,b)