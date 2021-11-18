import os
'''重命名'''
os.rename("config/a.txt","config/b.txt")
'''删除文件'''
os.remove("config/b.txt")
'''删除文件夹'''
os.removedirs("config")
'''创建文件夹'''
os.mkdir("config")
