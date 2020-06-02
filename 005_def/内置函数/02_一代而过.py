
# 了解

# eval    
#剥去字符串的外衣，执行里面的代码,危险 别用
s1 = '1+3' 
print(eval(s1))  #4


# exec
# 与evel几乎一样，处理代码流
s2 = '''
for i in [1,2,3]:
    print(i)
'''
exec(s2)


# hash   
# 获取一个对象的hash值
print(hash('shf'))  # 4709462226125274219


# help
# 查看函数或模块的详细说明
# print(help(list))
print(help(str.upper))


### callable
# 检查一个对象是否可调用
# 如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
def a():
    pass
print(callable(a))


# int  
# 函数用于将一个字符串或数字转换为整型。
print(int(3.3))


# float
# 函数用于将整数和字符串转换成浮点数。
print(float(2))


# complex  
# 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数。。
print(complex(2,4))


## bin：将十进制转换成二进制并返回。
print(bin(123))  # 0b1111011

## oct：将十进制转化成八进制字符串并返回。
print(oct(120))

## hex：将十进制转化成十六进制字符串并返回。
print(hex(123))


# divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
print(divmod(10,3))  # (3, 1)


# round：保留浮点数的小数位数，默认保留整数。
print(round(3.1415,2))  # 3.14
print(round(7/3))  # 2


# pow：求x**y次幂。（三个参数为x**y的结果对z取余）
print(pow(2,3))  # 8
print(pow(2,3,3))  # 三个参数为2**3次幂，对3取余。


# bytes 不同编码之间的转化
s = '你好'
bs = s.encode('utf-8')    #编码
print(bs)
s1 = bs.decode('utf-8')   #解码
print(s1)
bs = bytes(s,encoding='utf8')
print(bs)


# ord :输入字符查找字符编码的位置
print(ord('a'))
print(ord('中'))
# chr 输入位置找出其对应的字符
print(chr(97))
print(chr(20013))


# repr 返回一个对象的string形式
ss = '嘤嘤嘤'
print('%r' %ss)
print(repr(ss))
print(repr('{"name":"alex"}'))
print('{"name":"alex"}')


# all 可迭代对象中 全是True 才是 True
# any 可迭代对象中 有一个true  就是 true
print(all([1,'2s','']))
print(any([1,'2s','']))







