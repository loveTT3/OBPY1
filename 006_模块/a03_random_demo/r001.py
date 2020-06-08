# 常用模块random
import random
'''
提供随机数获取的相关方法
'''

# 获取 [0.0 , 1.0)内随机浮点数
# round(a,2)  字符串a保留两位小数
print(round(random.random(),2))
print(random.random())

#获取[2,22]之间的整数
print(random.randint(2,22))
#获取[1,10)之间的奇数
print('1-10之间的奇数: ',random.randrange(1,10,2))


#获取范围内的随机浮点数 [)
print(random.uniform(1,2))

#打乱顺序
a = [1,2,3,4,5]
print(a)
random.shuffle(a)
print(a)

#从x中随机抽取k个数据  组成一个列表返回
l1 = list(range(10))
print('随机生成一个列表：',random.sample(l1,3))

# 随机选择一个返回
print('随机选取一个返回：',random.choice(1,['a','b','c'],'23'))

#

