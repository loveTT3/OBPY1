# collections模块
'''
在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。
1.namedtuple: 生成可以使用名字来访问元素内容的tuple
2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
3.Counter: 计数器，主要用来计数
4.OrderedDict: 有序字典
5.defaultdict: 带有默认值的字典
'''

# namedtuple
import collections
point = collections.namedtuple('介绍',['x','y'])
p = point(1,2)
print(p.x)
print(p.y)

# counter
c = collections.Counter('adderfcdcadsadasw')
print(c)
