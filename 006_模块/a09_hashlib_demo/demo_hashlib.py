# hashlib 
'''
封装加密的类
工作原理：它通过一个函数，把任意长度的数据按照一定规则转换为一个固定长度的数据串（通常用16进制的字符串表示）。
特点：
    把一个大的数据切分成不同块，分别对不同块加密，再汇总结果和直接对整体数据加密的结果是一样的
    bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串
    不同的bytes类型数据转化成的结果一定不同。
    相同的bytes类型数据转化成的结果一定相同。
    此转化过程不可逆。
    原始数据一点小的变化，将导致加密结果非常大的差异
'''
import hashlib

str1 = 'abc中文'
# 获取一个加密对象
m = hashlib.md5()
# 使用update方法进行加密
m.update(str1.encode('utf-8'))
# 使用hexdigest方法获取加密结果
m2 = m.hexdigest()
print(m2)  # 1af98e0571f7a24468a85f91b908d335


# 把一个大的数据切分成不同块，分别对不同块加密，再汇总结果和直接对整体数据加密的结果是一样的
str2 = 'abc'
str3 = 'qwe'
str4 = str2+str3
m3 = hashlib.md5()
m3.update(str2.encode('utf-8'))
m3.update(str3.encode('utf-8'))
print(m3.hexdigest())
m4 = hashlib.md5()
m4.update(str4.encode('utf-8')) 
print(m4.hexdigest(),type(m4.hexdigest()))
print(m4.hexdigest() == m3.hexdigest())



# 加盐加密
# 固定的盐
ret = hashlib.md5('固定的盐'.encode('utf-8'))
ret.update('a'.encode('utf-8'))
print(ret.hexdigest())
# 动态的盐
username = '我叫孙悟空'
ret = hashlib.md5(username[0:3].encode('utf-8'))





