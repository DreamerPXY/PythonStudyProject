'''打开文件'''

file = open("config/a.txt","w+")

'''写入文件'''
file.write("hello world")

'''关闭文件'''
file.close()


'''读取文件'''
f = open("config/a.txt","r")
s = f.readline(1024)
print(s)
s = f.readline(1024)
print(s)

file.close()