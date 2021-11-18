str1 = "abcdefg"
list = [0,1,2,3,"3"]
tuple = (1,2,3)
set = {1,2,3}
print(type(set))
i = 3
print(str1 + str(i))
len(str1)
print("a" in str1)
print("3" in list)
print(list + list)
print("-"*100)

'''公共方法：range and e'''

for i in range(len(str1)):
    print(i)
    print(str1[i])
print("-"*100)
for i,char in enumerate(str1,start=1):
    print(i,char)
