import d001
import sys



d001.timee()
print(sys.path)

# 打印当前文件的路径
print(__file__)

import os
# 当前文件的相对路径
print(os.path.dirname(__file__)+r'/a01')




'''
aa在另一个文件夹  直接导入会报错

获取当前文件父路径  加上文件夹名字
添加到sys.path中
'''
a = os.path.dirname(__file__)+r'/a01'
sys.path.append(a)
import aabb