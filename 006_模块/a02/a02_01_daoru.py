
#导入模块的多种方式
'''
import aa    导入模块中的所有成员
import aaaa,bbb     一次性导入多个模块的所有成员 不推荐
from xx import yy   从某个模块导入指定的成员
from xx import a,b,c
from xx import *    从某一模块导入所有成员
'''

'''
import a 和 from xx import * 区别
1.第一种使用其中成员时，必须使用模块名作为前缀   不容易产生命名冲突
2.第二回中使用其中成员时，直接使用成员名即可   容易产生命名冲突，后定义的成员生效
'''
 
'''
避免重名  使用 alias
import aa  as  b
'''
 

'''
from xx  import x  控制成员被导入
在被导入模块写  
__all__ = ['age1','age2']  
列表 内容是可以被导入的成员名

但是  如果用import导包的话 会全部导入  绕过__all__
'''
import os,sys
a = os.path.dirname(__file__)
print(a)
a2 = os.path.dirname(a) + r'/a01'
print(a2)
qq = sys.path.append(a2)
from aabb import *
print(age1,age2)
# print(age3)  # 这行代码报错 因为 __all__列表里面 没有age3



'''
相对导入



'''



