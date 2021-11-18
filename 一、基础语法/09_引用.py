'''测试引用'''

"""
只有list set 和 元组才可以改变引用
"""
'''int 值不可以改变'''
a = 1
b = a
print(id(a))
print(id(b))

a = 2
print(b)
print(id(a))
print(id(b))

print("-"*60)
'''list 可以改变'''

listA = [1,2,3]
listB = listA

print(id(listA))
print(id(listB))

listA.append(4)
print(listB)

print(id(listA))
print(id(listB))


"""***测试函数传递问题***"""

def count_sum (a):
    a += a

a = 1
count_sum(a)
print(a)

s = "1"
count_sum(s)
print(s)

l = [1,2]
count_sum(l)
print(l)