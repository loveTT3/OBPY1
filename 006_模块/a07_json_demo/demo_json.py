# 序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去。
# 它的主要用途：文件读写数据，网络传输数据。

#json: 将数据转换成字符串，用于存储或者网络传输
# 用于网络传输：dumps、loads
# 用于文件写读：dump、load


import json

s =  json.dumps([1,2,3])  # 将指定对象转换成json字符串
print(type(s),s)  # '[1,2,3]'
 
s1 = json.dumps((1,2,3))  # 元祖被序列化后成为列表
print(type(s1),s1)

s4 = json.dumps({'a':1,'b':'mm'})  # 字典被序列化后成为字符串
print(type(s4),s4)

s2 = json.dumps(11)  # int被序列化后成为字符串
print(type(s2),s2)

# s3 = json.dumps(set('a'))  # 集合不能被序列化 TypeError: Object of type set is not JSON serializable
# print(type(s3),s3)

# 将json结果写到文件中
# with open(r'E:\PYXUEXI\OBPY1\006_模块\a07_json_demo\a.txt',mode='w',encoding='utf-8') as f:
#     json.dump([1,2,3],f)


# 反序列化
res = json.dumps([1,2,3])
lst = json.loads(res)
print(type(lst))
print('反序列化：',lst)

res1 = json.dumps((1,2,3))  #元组序列化再反序列化  回来后丢失原数据类型，变成列表
lst1 = json.loads(res)
print(type(lst1))
print('反序列化：',lst1)

# with open('a.txt',mode='w',encoding='utf-8') as ff:
#     json.dump([1,2,3],ff)
#     res = json.load(ff)
#     print(type(res))
#     print(res)


# 总结py
'''
json.dumps(obj)
json.dump(obj,f)
json.loads(s)
json.load(f)
'''

# json文件通常都是一次性写，一次性读

with open('json.txt',mode='w',encoding='utf-8') as f:
    f.write(json.dumps([1,2,3]) + '\n')
    f.write(json.dumps([4,5,6]) + '\n')


with open('json.txt',mode='r',encoding='utf-8') as f:
    for i in f:
        print(json.loads(i.strip()))
