#  内置函数

# print
''' 源码分析
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
    sep:   打印多个值之间的分隔符，默认为空格
    end:   每一次打印的结尾，默认为换行符
    flush: 立即把内容输出到流文件，不作缓存
    """
'''
print(111,222,333,sep='*')  # 111*222*333​
print(111,end='')
print(222)  #两行的结果 111222
f = open('a','w',encoding='utf-8')
print('写入文件',file=f,flush=True)

'''
int():pass
str():pass
bool():pass
set(): pass
list() 将一个可迭代对象转换成列表
tuple() 将一个可迭代对象转换成元组
dict() 通过相应的方式创建字典。
'''


# abs :返回绝对值
print(abs(-3))


# sum 求和
print(sum([1,2,3]))
print(sum((1,2,3),10))


# reversd 将一个序列翻转  返回翻转序列的新的迭代器
l = reversed('你好')
print(next(l))
print(list(l),type(l))


# zip  拉链方法  函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回，
lst1 = [1,2,3]
lst2 = '你说啥'
lst3 = ('a','b','c')
cap = zip(lst1,lst2,lst3)
for i in cap:
    print(i)


s = '你好太白'
bs = s.encode('utf-8')
print(bs)
# 结果:b'\xe4\xbd\xa0\xe5\xa5\xbd\xe6\xad\xa6\xe5\xa4\xa7'

s1 = bs.decode('utf-8')
print(s1)
# 结果: 你好太白

s = '你好'
bs = bytes(s,encoding='utf-8')
print(bs)
# 将字符串转换成字节
bs1 = str(bs,encoding='utf-8')
print(bs1)
# 将字节转换成字符串





'''
# 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，
# 然后通过你设定的返回值比较大小，返回最小的传入的那个参数。
'''

# min 求最小值  max  求最大值
print(min([1,2,3,-4]))  # -4
print(min([1,2,3,-4],key=abs))  #1  返回绝对值最小的数 
print(min(1,2,3,4,5,key = lambda x : abs(x-2)))
dic = {'a':3,'b':2,'c':1}
print(min(dic,key=lambda x: dic[x]))


# sorted 排序函数，产生新列表 从低到高
'''
语法:sorted(iterable,key=None,reverse=False)
iterable : 可迭代对象
key: 排序规则(排序函数),在sorted内部会将可迭代对象中的每一个元素传递给这个函数的参数.根据函数运算的结果进行排序
reverse :是否是倒叙,True 倒叙 False 正序
'''
dic1 = {'a':33,'b':22,'c':54,'d':39}
print(sorted(dic1,key=lambda x : dic1[x]))
l1 = [('a',11),('b',34),('c',22)]
print(sorted(l1,key=lambda x : x[1],reverse = True))  #从高到低


# filter 筛选过滤  返回的是迭代器
'''
语法: filter(function,iterable)
function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,然后根据function返回的True或者False来判断是否保留此项数据
iterable:可迭代对象
'''
l2 = [1,2,3,4,6,5,8,7]
print([i for i in l2 if i >3])  # 列表推导式 返回的是列表
xx = filter(lambda i : i > 3 , l2)  #筛选过滤  返回的是迭代器
print(xx)
print(list(xx))


# map 映射函数
'''
映射函数
语法: map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别取执行function
计算列表中每个元素的平方,返回新列表
'''
l2 = [1,2,3,4]
print([i **2 for i in l2])  # 列表推导式 返回的是列表
xx = map(lambda i : i**2 , l2)  #筛选过滤  返回的是迭代器
print(xx)
print(list(xx))


# reduce 
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行
from functools import reduce
l2 = [1,2,3,4,5]
def jia(x,y):
    return x**2 + y
l = reduce(jia,l2)
print(l)



