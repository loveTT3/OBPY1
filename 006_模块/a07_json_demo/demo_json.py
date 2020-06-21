# json

#json: 将数据转换成字符串，用于存储或者网络传输

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
with open(r'E:\PYXUEXI\OBPY1\006_模块\a07_json_demo\a.txt',mode='w',encoding='utf-8') as f:
    f.write(s4)