print('加油')

#  aaa

#python中没有常量 一般将变量名大写 代表常量
NAME = '孙悟空'

#注释
'''注释'''
"""注释"""

#基本数据类型


#运算符
#and or  not  优先级  not>and>or

#x or y  x为真 值为x   x为假  值是y
# x and y  x为真 值为y   x为假 值为x

#非 0 即 true

print(1 > 2 and 3 or  6)

#int ---> bool
print(bool(1))
print(bool(0))


#编码
# gbk  中文占2字节
# utf-8  中文占3个字节


# bool  int  str 转换
#bool <--> int   true 1  false 0
#str <--> int      int(str1)   str(int1)

#bool <-- str   非空即true  空字符串为false
 


i = 48
print(i.bit_length())
