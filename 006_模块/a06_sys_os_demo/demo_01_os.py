# os: 和操作系统相关操作被封装在这个模块中


import os


# 获取当前工作目录
print(os.getcwd())
os.chdir('OBPY1')  # 改变工作目录，相当于cd
os.chdir('006_模块')
os.chdir('a06_sys_os_demo')
print(os.getcwd())


# 和文件操作相关，重命名，删除
# os.rename('dda','aaa')  # 修改文件名
# os.remove('aaa')    # 删除文件
# print(os.stat('demo_01_os.py'))  #获取文件或者目录信息

# 删除文件夹
# os.removedirs('dirname1')    #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
import shutil
# shutil.rmtree('name')     #强行删除文件夹下所有内容


# 和路径相关的操作  os.path
print('父目录：',os.path.dirname(r'd:/PYPYPY/OBPY1/006_模块/a06_sys_os_demo/demo_01_os.py'))  
print('文件名：',os.path.basename(r'd:/PYPYPY/OBPY1/006_模块/\
                                a06_sys_os_demo/demo_01_os.py'))  
print('路径中的路径和文件名切分开： ',os.path.split(r'd:/PYPYPY/OBPY1/006_模块/a06_s\
                                                    ys_os_demo/demo_01_os.py'))  # 返回元组

# 拼接路径
print('拼接的路径：',os.path.join('d:\\','aaa','bbb','c.txt'))

# 返回path规范化的绝对路径
print(os.path.abspath(r'a\b\c'))
print(os.path.abspath(r'd:\\c\v'))

# 判断（加）判断 
path = '路径'
os.path.isabs(path)     # 如果path是绝对路径，返回True
os.path.isfile(path)    # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)     # 如果path是一个存在的目录，则返回True。否则返回False



