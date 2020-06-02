#字典
#dict  3.5之前无序   3.6创建有序    
'''
不可变：int str   bool  tuple
可变： dict list set
'''
#键只能是不可变数据类型,且唯一
d = {1:'a',2:'b',3:'c'}




# 创建
d1 = dict(((1,2),('22',33),('dsa','dsad')))
print(d1)

d2 = dict(ondde=1,two=2,dsas=2)
print(d2)

d3 = dict({1:2,2:'dsa','dd':'ss'})
print(d3)

#字典的所有键来自一个可迭代对象，字典的值使用同一个值，共用一个值，一个改变 都改变
d4 = dict.fromkeys('asd',100)
print(d4)   #{'s': 100, 'd': 100, 'a': 100}

#增
d1 = dict(((1,2),('22',33),('dsa','dsad'))) 
d1['key'] = 'caluene'   #key不存在 则新增
d1[1] = '悟空'  #key存在，则更新

d1.setdefault('aa','aa')    #key不存在 则新增
d1.setdefault('aa','dsa')   #key存在 则不变
print(d1)

d1.update(name = '李白',age = 19) # key不存在更新  存在修改
d2 = {1:2}
d1.update(d2)
print(d1)
d2.update([(2,'a'),(3,'x'),(4,'c')])
print(d2)
#删
d2 = {'22': 33, 1: '悟空', 'key': 'caluene', 'dsa': 'dsad', 'aa': 'aa'}
d2.pop('22')
d2.pop('lll','没有此键')    #无论有没有key  都不报错，不存在则返回第二个参数

del d2['dsa']
# d2.clear()
print(d2)


#改
d1 = dict(((1,2),('22',33),('dsa','dsad'))) 
d1['key'] = 'caluene'   #key不存在 则新增
d1[1] = '悟空'  #key存在，则更新


#查
l  = d2.get('key','没有此键')   #有则查，没有显示第二个参数
print(l)

print('全是key： ',d2.keys())
print('全是calue： ',d2.values())
print('全是键值对 ',d2.items())

#可转换成列表
print(list(d2.keys()))
for i in d2.values():
    print(i)
#返回键值对
for i in d2.items():
    print(i)
    a , b = i
    print(a,'-',b)
# 利用了元组的拆包
for key,value in d2.items():        
    print(key,value)
    






#练习1
'''
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
请在k3对应的值中追加一个元素 44，输出修改后的字典
请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic['k4'] = 'v4'
dic['k1'] = 'alex'
dic['k3'].append('44')
dic['k3'].insert(1,'18')
print(dic)

dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
}
# 1. 获取汪峰的名字。
print(dic['name'])
# 2.获取这个字典：{'name':'国际章','age':38}。
print(dic['wife'])
# 3. 获取汪峰妻子的名字。
print(dic['wife'][0]['name'])
# 4. 获取汪峰的第三个孩子名字。
print(dic['children']['girl_three'])


#练习2
'''字典中所有键带k的键值对删除'''
dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
# 在循环一个字典的过程中，不要改变字典的大小（增，删字典的元素），这样会直接报错。
# l = []
# for i in dic.keys():
#     if 'k' in i:
#         l.append(i)
# print(l)
# for i in l:
#     dic.pop(i)
# print(dic)

for i in list(dic.keys()):
    if 'k' in i:
        dic.pop(i)
print(dic)



